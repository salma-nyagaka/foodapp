from django.shortcuts import render

# Create your views here.
import os
from django.shortcuts import redirect
from rest_framework import serializers, status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from ...helpers.constants import SUCCESS_MESSAGE, FORBIDDEN_MESSAGE
from ...helpers.renderers import RequestJSONRenderer
from .serializers import OrderSerializer, SingleOrderSerializer
from .models import Order
from .helpers.get_order_object import get_order_object


class OrderAPIView(generics.GenericAPIView):
    """ Class to add order items """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = SingleOrderSerializer

    def post(self, request):
        """ Method to add a new order """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if serializer.is_valid():
            return_message = {
                'message':
                SUCCESS_MESSAGE.format("Menu has been created"),
                "data": serializer.data
            }
            return Response(return_message, status=status.HTTP_201_CREATED)
        return_message = {
            'message': serializer.errors
        }
        return Response(return_message, status=status.HTTP_400_BAD_REQUEST)


class UsersOrdersPIView(generics.RetrieveAPIView):
    """ Class to get a user's orders"""
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = SingleOrderSerializer


    def get(self, request):
        """ Method to get a user's orders"""
        user_id = request.user.id
        data = Order.objects.filter(user_id=user_id).filter(status=False)
        serializer = self.serializer_class(data, many=True)

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("All order items have been fetched"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)
