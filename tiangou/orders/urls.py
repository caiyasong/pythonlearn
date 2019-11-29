from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^order/$', views.index, name='index'),
    url(r'^pay/(\w+)$', views.pay, name='pay'),
    url(r'^payback/$', views.payback, name='payback'),

]