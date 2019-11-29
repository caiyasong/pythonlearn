from django.http import JsonResponse


def reader_json(data='', code=0):
    return JsonResponse({'code': code, 'data': data})




def check_perm(perm_name):
    def outer(func):
        def inner(request, *args, **kwargs):
            # print('---', func.__name__)
            # 通过用户的vip_id 找到vip对应哪些权限
            perms = request.user.vip.all_perm
            perm_name_list = [perm.name for perm in perms]
            if perm_name in perm_name_list:
                return func(request, *args, **kwargs)
            else:
                return render_json('没有权限', error.NO_PERM)

        return inner

    return outer