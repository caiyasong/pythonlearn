from rest_framework.viewsets import ModelViewSet

from admins.serializers.order import OrderModelSerializer
from orders.models import Order


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer