from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from market.models import Goods
from users.models import User
from . import models


def index(request):
    tg = models.tg_tg.objects.all()[0:5]
    pp = models.tg_pp.objects.all()[0:14]
    tg1 = models.tg_tg.objects.all()[11:12]
    tg2 = models.tg_tg.objects.all()[13:18]
    tg3 = models.tg_tg.objects.all()[22:26]
    tg4 = models.tg_tg.objects.all()[26:38]
    zmgd = models.tg_zmgd.objects.all()[2:7]
    mid = models.tg_mid.objects.all()[5:19]
    mid1 = models.tg_mid.objects.get(id=18)
    gu = models.tg_gu.objects.all()
    gid = Goods.objects.all()


    data = {
        'tg':tg,
        'pp':pp,
        'tg1':tg1,
        'tg2':tg2,
        'tg3':tg3,
        'tg4':tg4,
        'zmgd':zmgd,
        'mid':mid,
        'mid1':mid1,
        'gu':gu,
        'gid':gid
    }

    return render(request, '天狗商城.html', data)