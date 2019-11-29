from django.conf.urls import url

from market import views

urlpatterns = [
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.index, name='index'),
    url('^savedata/$', views.savedata, name='savedata')

]