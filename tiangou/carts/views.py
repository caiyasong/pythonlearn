import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection

from market.models import Goods


def index(request):
    username = request.session.get('username')
    data = {}
    if username:
        redis_cli = get_redis_connection('cart')
        cartdata = redis_cli.get(username)

        cartdict = json.loads(cartdata.decode())
        # print(cartdata)
        good = Goods.objects.get(productid=cartdict.get('gid'))
        totalprice = float(good.marketprice) * int(cartdict.get('gnum'))
        order_code = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(good.productid)
        data ={
            'good': good,
            'gnum': cartdict.get('gnum'),
            'totalprice': totalprice,
            'order_code': order_code
        }
    return render(request, '我的购物车.html', data)