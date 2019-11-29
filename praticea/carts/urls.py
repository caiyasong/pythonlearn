from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^carts/$', views.index, name='index'),
    url(r'^selects/$', views.selects, name='selects')
]