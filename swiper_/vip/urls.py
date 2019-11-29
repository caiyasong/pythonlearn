from django.conf.urls import url

from . import api

urlpatterns = [
    url(r'^rank/$', api.rank)
]