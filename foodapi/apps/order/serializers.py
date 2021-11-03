from rest_framework import serializers
from .models import Order
from ..menu.serializers import MenuSerializer


class OrderSerializer(serializers.ModelSerializer):
    """ Serialize order data"""

    class Meta:
        model = Order
        fields = ('user', 'order')


class SingleOrderSerializer(serializers.ModelSerializer):
    """ Serialize single order data"""
    order =  MenuSerializer(many=False, read_only=True)
    class Meta:
        model = Order
        fields = ('__all__')
