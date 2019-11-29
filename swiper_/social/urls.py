from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^social/recommend/$', api.recommend),
    url(r'^user/like/$', api.like),
    url(r'^user/dislike/$', api.dislike),
    url(r'^user/superlike/$', api.superlike),
]