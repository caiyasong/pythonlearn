import datetime
import os


from alipay import AliPay
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.http import require_POST
from django_redis import get_redis_connection

from market.models import Goods
from orders.models import Orders
from tiangou import settings
from users.models import User


@require_POST
def index(request):
    if request.method == 'POST':
        username = request.session.get('username')
        user = User.objects.get(username=username)
        userid = user.id
        gid = request.POST.get('order_code')
        gnum = request.POST.get('gnum')
        totalprice = request.POST.get('totalprice')
        price = request.POST.get('price')
        Orders.objects.create(
            uid=userid,
            gid=gid,
            gnum=gnum,
            totalprice=totalprice,
            price=price
        )
        return JsonResponse({'data': 'ok'})


def pay(request, order_code):
    order = Orders.objects.get(gid=order_code)
    total_amount = order.totalprice
    alipay = AliPay(
        appid='2016101400684357',
        app_notify_url=None,  # 默认回调url
        app_private_key_path=os.path.join(settings.BASE_DIR, "alipay/app_private_key.txt"),
        alipay_public_key_path=os.path.join(settings.BASE_DIR, "alipay/alipay_public_key.txt"),
        sign_type='RSA2',
        debug=True
    )

    # 生成登录支付宝连接
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_code,
        total_amount=float(total_amount),
        subject='商品支付信息',
        return_url='http://127.0.0.1:8000/payback/',
    )

    alipay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return redirect(alipay_url)
    # return HttpResponse('ok')

def payback(request):
    query_dict = request.GET
    data = query_dict.dict()

    # 获取并从请求参数中剔除signature
    signature = data.pop('sign')

    # 创建支付宝支付对象
    alipay = AliPay(
        appid='2016101400684357',
        app_notify_url=None,  # 默认回调url
        app_private_key_path=os.path.join(settings.BASE_DIR, "alipay/app_private_key.txt"),
        alipay_public_key_path=os.path.join(settings.BASE_DIR, "alipay/alipay_public_key.txt"),
        sign_type="RSA2",
        debug=True
    )
    # 校验这个重定向是否是alipay重定向过来的
    success = alipay.verify(data, signature)
    if success:
        order_code = data['out_trade_no']
        return HttpResponse('支付成功')
    else:
        # 验证失败
        return HttpResponse('支付失败')