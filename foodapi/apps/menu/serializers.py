from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    """ Serialize menu data"""
    class Meta:
        model = Menu
        fields = ('name', 'price', 'description')


class SingleMenuSerializer(serializers.ModelSerializer):
    """ Serialize single menu data"""

    class Meta:
        model = Menu
        fields = ('__all__')