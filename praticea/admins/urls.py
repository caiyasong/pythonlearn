from django.conf.urls import url

from admins import views

from .view import user
from .view import order

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^userinfo/$', user.UserInfo.as_view()),
    url(r'^user/$', user.User.as_view()),
    url(r'^order/$', order.OrderModelViewSet.as_view({'get': 'list'})),
    url(r'^order/(?P<pk>\d+)/$', order.OrderModelViewSet.as_view({'get': 'retrieve', 'put': 'update'}))

]