import re

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.http import require_POST

from users.models import User


def register(request):
    if request.method == 'GET':
        return render(request, '注册.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        Txtidcode = request.POST.get('Txtidcode')
        idcode = request.POST.get('idcode')
        print(username)
        print(pwd2)
        print(pwd1)
        print(email)
        print(Txtidcode)
        print(idcode)

        idcode = re.findall(r'<font color=(.*)</font>', idcode, flags=re.I)
        idcode1 = idcode[0].split('>')
        str1 = ''
        for i in [idcode1[1], idcode1[3], idcode1[5]]:
            str1 += i[0]
        idcode = str1 + idcode1[-1]

        un = User.objects.filter(username=username).exists()
        if len(email) < 7:
            return HttpResponse('邮箱长度不合法')
        if not re.match(r'^([a-zA-Z\.0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', email):
            return HttpResponse('邮箱格式错误')

        if un:
            return HttpResponse('用户名已存在')

        if len(pwd1) < 4 or len(pwd1) > 20:
            HttpResponse('密码长度不合法')

        if not re.findall(r'(\w+)', pwd1):
            return HttpResponse('密码不合法')

        if pwd1 != pwd2:
            return HttpResponse('两次密码不一致')

        if Txtidcode != idcode:
            return HttpResponse('验证码输入错误')

        user = User.objects.create(
            username=username,
            password=make_password(pwd1),
            email=email,
        )

        return JsonResponse({'data': 'ok'})

@require_POST
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if not user.exists():
            return HttpResponse('用户名不存在')

        if not check_password(password, user[0].password):
            return HttpResponse('密码不正确')


        request.session['username'] = username

        return JsonResponse({'data': 'ok'})


