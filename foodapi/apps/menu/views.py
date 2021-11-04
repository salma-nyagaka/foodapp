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
from .serializers import MenuSerializer, SingleMenuSerializer
from .models import Menu
from .helpers.get_menu_object import get_menu_object


class MenuAPIView(generics.GenericAPIView):
    """ Class to add menu items and get all menu items """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = MenuSerializer

    def post(self, request):
        """ Method to add a new menu """
        is_admin = request.user.is_superuser
        if is_admin:
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
        return_message = {
            'message':FORBIDDEN_MESSAGE
        }
        return Response(return_message, status=status.HTTP_403_FORBIDDEN)

class AllMenuItemsPIView(generics.RetrieveAPIView):
    """ Class to get all menu items"""
    serializer_class = SingleMenuSerializer

    def get(self, request):
        """ Method to get all menu items """

        data = Menu.objects.all()
        serializer = self.serializer_class(data, many=True)

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("All menu items have been fetched"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)


class SingleMenuAPIView(generics.RetrieveAPIView):
    """ Class to get, update, delete a single menu item"""
    serializer_class = SingleMenuSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, menu_id):
        """ Method to get a single menu item """
        data = get_menu_object(menu_id)
        serializer = self.serializer_class(data)

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("Menu item has been fetched"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)

    def put(self, request, menu_id):
        """ Method to update a single menu item """
        is_admin = request.user.is_superuser
        if is_admin:
            question_obj = get_menu_object(menu_id)
            serializer = self.serializer_class(
                question_obj, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return_message = {
                'message': SUCCESS_MESSAGE.format("The menu item has been updated"),
                "data": serializer.data
            }
            return Response(return_message, status=status.HTTP_200_OK)
            
        return_message = {
            'message':FORBIDDEN_MESSAGE
        }
        return Response(return_message, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, menu_id):
        """ Method to delete a single menu item """
        is_admin = request.user.is_superuser
        if is_admin:
            data = Menu.objects.get(id=menu_id)
            data.delete()
            return_message = {
                'message':
                SUCCESS_MESSAGE.format("Menu item has been deleted")
            }
            return Response(return_message, status=status.HTTP_201_CREATED)
        return_message = {
            'message':FORBIDDEN_MESSAGE
        }
        return Response(return_message, status=status.HTTP_403_FORBIDDEN)
