from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='index'),
    url(r'^login/$', views.login, name='login'),
]