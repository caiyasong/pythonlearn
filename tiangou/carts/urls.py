from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^carts/$', views.index, name='index')
]