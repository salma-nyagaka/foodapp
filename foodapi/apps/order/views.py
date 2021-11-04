from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...helpers.constants import SUCCESS_MESSAGE, FORBIDDEN_MESSAGE
from ...helpers.renderers import RequestJSONRenderer
from .serializers import SingleOrderSerializer, SingleDetailsOrderSerializer, OrderSerializer
from .models import Order
from .helpers.get_order_object import get_order_object, get_user_order_object


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
        if user_role == 'FOOD_ATTENDANT' or 'ADMIN':
            data = get_order_object()
            serializer = self.serializer_class(data, many=True)
            return_message = {
                'message':
                SUCCESS_MESSAGE.format("All pending orders have been fetched"),
                "data": serializer.data
            }
            return Response(return_message, status=status.HTTP_200_OK)
        return_message = {
            'message':FORBIDDEN_MESSAGE
        }
        return Response(return_message, status=status.HTTP_403_FORBIDDEN)

class SingleOrderAPIView(generics.RetrieveAPIView):
    """ Class to update an order status"""
    serializer_class = SingleDetailsOrderSerializer
    permission_classes = (IsAuthenticated,)
    # queryset = Order.objects.all()

    def update(self, request, pk):
        """ Method to update order status by food attendant"""
        user_role = request.user.role
        if user_role == 'FOOD_ATTENDANT':
            data = get_order_object(pk)
            serializer = self.serializer_class(data, partial=True)
            serializer.save()

            return_message = {
                'message':
                SUCCESS_MESSAGE.format("Menu item has been updated"),
                "data": "k"
            }
            return Response(return_message, status=status.HTTP_201_CREATED)
        return_message = {
            'message':FORBIDDEN_MESSAGE
        }
        return Response(return_message, status=status.HTTP_403_FORBIDDEN)
