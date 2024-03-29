from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...helpers.constants import SUCCESS_MESSAGE, FORBIDDEN_MESSAGE
from ...helpers.renderers import RequestJSONRenderer
from ...helpers.validate_user import validate_attendant, validate_attendant_or_admin
from .serializers import SingleOrderSerializer, SingleDetailsOrderSerializer, OrderSerializer
from .helpers.get_order_object import get_order_object, get_user_order_object
from.helpers.update_status import update_status
from .models import Order
class OrderAPIView(generics.GenericAPIView):
    """ Class to add order items """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = OrderSerializer

    def post(self, request):
        """ Method to add a new order """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # if serializer.is_valid():
        return_message = {
            'message':
            SUCCESS_MESSAGE.format("Your order has been created"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)


class UsersOrdersPIView(generics.RetrieveAPIView):
    """ Class to get a user's orders"""
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = SingleOrderSerializer

    def get(self, request):
        """ Method to get a user's orders"""
        user_id = request.user.id
        params = request.query_params
        data = get_user_order_object(params, user_id)
        serializer = self.serializer_class(data, many=True)

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("Your orders have been fetched"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)


class AllOrdersPIView(generics.RetrieveAPIView):
    """ Class to get all orders"""
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = SingleOrderSerializer

    def get(self, request):
        """ Method to get all orders"""
        user_role = request.user.role
        params = request.query_params
        validate_attendant_or_admin(user_role)
        data = get_order_object(params)
        serializer = self.serializer_class(data, many=True)
        return_message = {
            'message':
            SUCCESS_MESSAGE.format("All pending orders have been fetched"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_200_OK)


class SingleOrderAPIView(generics.RetrieveUpdateAPIView):
    """ Class to update an order status"""
    permission_classes = (IsAuthenticated,)
    serializer_class = SingleDetailsOrderSerializer

    def update(self, request, pk):
        """ Method to update order status by food attendant"""
        user_role = request.user.role
        validate_attendant(user_role)
        data = Order.objects.get(id=pk)
        params = request.query_params
        status_update = update_status(data,params)
        serializer_data = self.serializer_class(status_update)

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("Order status has been updated"),
            "data": serializer_data.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)
