from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """ Serialize order data"""

    class Meta:
        model = Order
        fields = ('user', 'order')


class SingleOrderSerializer(serializers.ModelSerializer):
    """ Serialize single order data"""

    class Meta:
        model = Order
        fields = ('__all__')
