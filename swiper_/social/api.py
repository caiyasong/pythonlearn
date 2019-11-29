import datetime
import random

from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from common.func import reader_json
from social.models import Swiped, Friend
from user.models import User



def recommend(request):
    max_year = datetime.date.today().year - request.user.profile.min_dating_age
    min_year = datetime.date.today().year - request.user.profile.max_dating_age

    users = User.objects.filter(
        location=request.user.profile.location,
        sex=request.user.profile.dating_sex,
        birth_year__lte=max_year,
        birth_year__gte=min_year
    ).exclude(id=request.user.id)

    swiped = Swiped.objects.filter(uid=request.user.id)
    sidlist = [i.sid for i in swiped]

    users = users.exclude(id__in=sidlist)

    # users = users.order_by('?')[:20]

    lis = list(range(0, users.count()))
    sam = random.sample(lis, 10)
    users = [users.all()[i] for i in sam]

    data = []
    for user in users:
        data.append(model_to_dict(user))

    return reader_json(data)


def like(request):

    sid = request.POST.get('sid')

    Swiped.add_swiped(request.user.id, sid, 'like')

    Swiped.get_friend(request.user.id, sid)

    return reader_json('success')


def dislike(request):
    sid = request.POST.get('sid')

    Swiped.add_swiped(request.user.id, sid, 'dislike')


    return reader_json('success')


def superlike(request):
    sid = request.POST.get('sid')

    Swiped.add_swiped(request.user.id, sid, 'superlike')

    Swiped.get_friend(request.user.id, sid)

    return reader_json('success')



def rewind(request):


    # 把反悔的 数量 存在 redis里面
    # 判断一天之内，反悔的数量为3
    # 有效期（单位是秒），就是整天的时间-当前的时间 24*3600 - 小时*3600 - 分钟*60 - 秒

    redis_cli = get_redis_connection()
    # 反悔的次数，如果有redis就直接拿出来加1，如果没有就默认取1
    uid = request.user.id
    num = redis_cli.get(f"rewind-{uid}")
    if not num:
        num = 0
    else:
        num = int(num.decode())
    # num = 0 if num == 0 else num.decode()

    if num < 3:

        num += 1

        # 过期时间
        now = datetime.datetime.now()
        rewind_time = 24*3600 - now.hour*3600 - now.minute*60 - now.second

        redis_cli.set(f"rewind-{uid}", num, rewind_time)

        # 获取上一次滑动记录
        lastRow = Swiped.objects.filter(uid=request.user.id).last()

        # 如果是不喜欢的记录，直接删除滑动记录
        if lastRow.mark == 'dislike':
            lastRow.delete()
        else:
            # 如果是好友，解除好友记录
            uid1 = min(request.user.id, lastRow.sid)
            uid2 = max(request.user.id, lastRow.sid)
            Friend.objects.filter(uid1=uid1, uid2=uid2).delete()

            # 删除滑动记录
            lastRow.delete()

        return render_json('成功')

    else:

        return render_json('超过反悔次数', error.BEYOND_REWIND_NUM)