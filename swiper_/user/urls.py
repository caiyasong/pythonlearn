from django.conf.urls import url

from . import api

urlpatterns = [
    url(r'^user/login/$', api.login),
    url(r'^user/sms/$', api.sms),
    url(r'^user/avatar/$', api.avatar),
]