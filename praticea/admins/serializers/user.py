from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from orders.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'avtar': {'default': '', 'required': False}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)