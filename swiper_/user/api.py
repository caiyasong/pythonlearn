import json
import os
import re

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views import View

from common.func import reader_json
from common import error
from lib.yzx import send_sms
from django_redis import get_redis_connection

from swiper_ import settings
from user.models import User, Profile


def sms(request):
    phone = request.POST.get('phone')
    if not re.match(r'^1[3456789]\d{9}$', phone):
        return reader_json('手机号格式错误', error.PHONE_FORMAT_ERROR)

    send_sms.delay(phone)

    return JsonResponse({'响应成功'})


def login(request):
    phone = request.POST.get('phone')
    # print(phone)
    # code = request.POST.get('code')

    # if not re.match(r'^1[3456789]\d{9}$', phone):
    #     return reader_json('手机号格式错误', error.PHONE_FORMAT_ERROR)
    #
    # redis_cli = get_redis_connection()
    # redis_code = redis_cli.get(f'sms-code{phone}')
    #
    # if not redis_code:
    #     return reader_json('验证码过期', error.SMSCODE_EXPIRED)
    #
    #
    # if code != redis_code.decode():
    #     return reader_json('验证码输入错误', error.SMSCODE_ERROR)

    user, created = User.objects.get_or_create(phonenum=phone, defaults={'nickname': phone})

    # print(user, created)

    request.session['uid'] = user.id

    # dic = {}
    # fields = User._meta.get_fields()
    # for field in fields:
    #     name = field.attname
    #     dic[name] = getattr(user, name)

    datas = model_to_dict(user)
    return reader_json(datas)


def avatar(request):

    img = request.FILES.get('avatar')
    ext = os.path.splitext(img.name)[1]
    img_name = f'avatar-{request.user.id}{ext}'
    img_path = f'/uploads/{img_name}'
    with open(os.path.join(settings.MEDIA_ROOT, img_name), 'ab') as fp:
        for chunk in img.chunks():
            fp.write(chunk)
    return reader_json(img_path)


class ProfileView(View):
    def get(self, request):
        profile = request.user.profile

        profile = model_to_dict(profile)

        return reader_json(profile)

    def put(self, request):
        # 1, 获取数据
        data = json.loads(request.body)

        location = data.get('location')
        min_distance = data.get('min_distance')
        max_distance = data.get('max_distance')
        min_dating_age = data.get('min_dating_age')
        max_dating_age = data.get('max_dating_age')
        dating_sex = data.get('dating_sex')

        # 2，判断数据
        # 判断数据都不能为空
        if not all([location, min_distance, max_distance, min_dating_age, max_dating_age, dating_sex]):
            return reader_json('交友数据不能为空', error.PROFILE_NOT_EMPTY)

        # 最小距离不能大于最大距离
        if min_distance > max_distance:
            return reader_json('最小距离不能大于最大距离', error.MIN_DIATANCE_GT_MAX_DISTANCE)

        # 最小年龄不能大于最大年龄
        if min_dating_age > max_dating_age:
            return reader_json('最小年龄不能大于最大年龄', error.MIN_AGE_GT_MAX_AGE)

        # 3,处理逻辑

        # 更新数据
        Profile.objects.filter(id=request.user.id).update(
            location=location,
            min_distance=min_distance,
            max_distance=max_distance,
            min_dating_age=min_dating_age,
            max_dating_age=max_dating_age,
            dating_sex=dating_sex
        )

        datas = model_to_dict(request.user.profile)

        # 4,返回响应
        return reader_json(datas)
