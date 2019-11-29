from django.http import HttpResponse
from django.shortcuts import render
from .models import AxfWheel, AxfNav, AxfShop, MustBuy

# Create your view here.
def index(request):
    wheel = AxfWheel.objects.all()
    nav = AxfNav.objects.all()
    mustbuy = MustBuy.objects.all()
    shop1 = AxfShop.objects.all()[0:1]
    shop2 = AxfShop.objects.all()[1:3]
    shop3 = AxfShop.objects.all()[3:7]
    shop4 = AxfShop.objects.all()[7:11]

    data = {
        'wheels': wheel,
        'navs': nav,
        'mustbuys': mustbuy,
        'shops1': shop1,
        'shops2': shop2,
        'shops3': shop3,
        'shops4': shop4,

    }



    return render(request, 'home.html', data)