from rest_framework import serializers

from orders.models import Order


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

        read_only_fields = ('uid', 'order_code', 'total_count', 'total_amount')