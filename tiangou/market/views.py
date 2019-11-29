import json

from django.http import HttpResponse, JsonResponse


# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from django_redis import get_redis_connection

from market.models import Goods


def detail(request, gid):
    flag = 'False'
    if request.session.get('username'):
        flag = 'True'
    gid_ = Goods.objects.get(productid=gid)
    data = {
        'gid': gid_,
        'flag': flag
    }

    if gid == 'P20160313145249235':
        return render(request, '商品详情.html', data)
    elif gid == 'P20160313153110796':
        return render(request, '商品详情2.html', data)
    elif gid == 'P20160312150857107':
        return render(request, '商品3.html', data)
    elif gid =='P20160312144947839':
        return render(request, '商品4.html', data)


def savedata(request):
    gid = request.POST.get('gid')
    gnum = request.POST.get('gnum')
    username = request.session.get('username')
    redis_cli = get_redis_connection('cart')

    cartdata = {'gid': gid, 'gnum': gnum}
    data = json.dumps(cartdata)
    redis_cli.set(username, data)

    return JsonResponse({'data': 'ok'})


