import datetime
import json
import os

from Cryptodome.PublicKey import RSA
from alipay import AliPay
from django.conf import settings
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your view here.
from django.urls import reverse
from django_redis import get_redis_connection

from market.models import Goods
from orders.models import User, Order, OrderDetail


def index(request):
    if not request.session.get('username'):
        return redirect(reverse('users:login'))

    username = request.session.get('username')
    redis_cli = get_redis_connection('cart')
    cart_data = json.loads(redis_cli.get(f'cart-{username}'))

    cart_dict = {}

    for cart in cart_data:
        if cart_data[cart]['selected'] == '1':
            cart_dict[int(cart)] = int(cart_data[cart]['count'])

    with transaction.atomic():
        save_id = transaction.savepoint()
        user = User.objects.get(username=username)

        order_code = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(user.id)

        order = Order.objects.create(
            uid = user.id,
            order_code = order_code,
            total_count = sum(cart_dict.values()),
            total_amount = 0,
            status = 1
        )

        totalprice = 0
        for gid,count in cart_dict.items():

            while True:
                good = Goods.objects.get(id=gid)

                if count > good.storenums:
                    transaction.savepoint_rollback(save_id)
                    return HttpResponse('当前库存不足')

                res = Goods.objects.filter(id=good.id, storenums=good.storenums).update(
                    storenums=good.storenums - count,
                    productnum=good.productnum + count
                )

                if not res:
                    continue

                OrderDetail.objects.create(
                    uid=user.id,
                    order_code=order_code,
                    goods_id=gid,
                    counts=count,
                    price=good.price,
                    )

                totalprice += good.price * count

                del cart_data[str(gid)]

                break

        order.total_amount = totalprice
        order.save()

        redis_cli.set(f'cart-{username}', json.dumps(cart_data))

        transaction.savepoint_commit(save_id)


    # return HttpResponse('生成订单成功')
    return redirect(reverse('orders:orderpay', args=(order_code, )))

def not_pay(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)

    orders = Order.objects.filter(uid=user.id, status=1)


    data_dict = {}
    for order in orders:

        data_list = []
        orderdetails = OrderDetail.objects.filter(order_code=order.order_code)
        for orderdetail in orderdetails:

            good = Goods.objects.get(id=orderdetail.goods_id)
            good_dict = {
                'img': good.productimg,
                'name': good.productlongname,
                'price': orderdetail.price,
                'count': orderdetail.counts
            }

            data_list.append(good_dict)

        data_dict[order.order_code] = data_list


    context = {
        'data_dicts': data_dict
    }


    return render(request, 'order_list_not_pay.html', context)


def orderpay(request, order_code):
    order = Order.objects.get(order_code=order_code)

    data = []

    orderdetails = OrderDetail.objects.filter(order_code=order_code)
    for orderdetail in orderdetails:
        good = Goods.objects.get(id=orderdetail.goods_id)
        good_dict = {
            'img': good.productimg,
            'name': good.productlongname,
            'price': orderdetail.price,
            'count': orderdetail.counts
        }

        data.append(good_dict)


    context = {
        'totalamount': order.total_amount,
        'datas': data,
        'order_code':order_code
    }

    return render(request, 'order_detail.html', context)


def pay(request, order_code):
    alipay = AliPay(
        appid='2016101400684357',
        app_notify_url=None,  # 默认回调url
        app_private_key_path=os.path.join(settings.BASE_DIR, "alipay/app_private_key.txt"),
        alipay_public_key_path=os.path.join(settings.BASE_DIR, "alipay/alipay_public_key.txt"),
        sign_type='RSA2',
        debug=True
    )
    order = Order.objects.get(order_code=order_code)

    # 生成登录支付宝连接
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_code,
        total_amount=float(order.total_amount),
        subject='商品支付信息',
        return_url='http://127.0.0.1:8000/payback/',
    )

    alipay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return redirect(alipay_url)


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
        Order.objects.filter(order_code=order_code).update(status=2)
        return HttpResponse('支付成功')
    else:
        # 验证失败
        return HttpResponse('支付失败')