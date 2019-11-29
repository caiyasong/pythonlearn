from django.conf.urls import url

from . import views

urlpatterns = [
    # url('^market/$', views.index, name='index'),
    url(r'^detail/(\w+)/$', views.detail, name='detail'),
    url(r'^savedata/$', views.savedata, name='savedata')
]