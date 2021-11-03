from rest_framework import serializers
from .models import Order
from ..menu.serializers import MenuSerializer
from ..authentication.serializers import  UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    """ Serialize order data"""

    class Meta:
        model = Order
        fields = ('user', 'order')


class SingleOrderSerializer(serializers.ModelSerializer):
    """ Serialize single order data"""
    order =  MenuSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Order
        fields = ('__all__')

class SingleDetailsOrderSerializer(serializers.ModelSerializer):
    """ Serialize single  data"""
    class Meta:
        model = Order
        fields = ('status')
