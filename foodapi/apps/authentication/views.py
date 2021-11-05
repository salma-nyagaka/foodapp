import os
from django.shortcuts import redirect
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ...helpers.constants import SUCCESS_MESSAGE, FORBIDDEN_MESSAGE
from ...helpers.renderers import RequestJSONRenderer
from ...helpers.validate_user import validate_admin
from .models import User
from .serializers import (
    LoginSerializer, RegistrationSerializer,
    UserSerializer)
from .backends import JWTAuthentication
from .helpers.get_user_obj import get_user_object
from .helpers.validate_params import validate_parans


class RoleAPIView(GenericAPIView):
    """Register a new user with a role"""
    # permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        """ Signup a new user """

        params = request.query_params
        validate_parans(params)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("Your account has been created"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        """Login a user"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = serializer.data

        user = User.get_user(user_data['email'])

        userdata = {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "role": user.role,
        }
        user_data['token'] = JWTAuthentication.generate_token(
            userdata=userdata)

        return_message = {
            'message': SUCCESS_MESSAGE.format("You have logged in"),
            "data": user_data,
            "token": user_data
        }
        return Response(return_message, status=status.HTTP_200_OK)


class AllUsersAPIView(generics.RetrieveAPIView):
    """ Class to get all users"""
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)

    def get(self, request):
        """ Method to get allusers """
        is_admin = request.user.is_superuser
        validate_admin(is_admin)
        data = User.objects.all().order_by('-created_at')
        serializer = self.serializer_class(data, many=True)

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("All users have been fetched"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)


class SingleUserAPIView(generics.RetrieveAPIView):
    """ Class to pdate, delete a single menu item"""
    serializer_class = LoginSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        """ Method to get a single user """
        is_admin = request.user.is_superuser
        validate_admin(is_admin)
        data = get_user_object(user_id)
        serializer = self.serializer_class(data)

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("User details have been fetched"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)

    # def put(self, request, user_id):
    #     """ Method to update a single user """
    #     is_admin = request.user.is_superuser
    #     if is_admin:
    #         question_obj = get_user_object(user_id)
    #         serializer = self.serializer_class(
    #             question_obj, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return_message = {
    #             'message':
    # SUCCESS_MESSAGE.format("User details have been updated"),
    #             "data": serializer.data
    #         }
    #         return Response(return_message, status=status.HTTP_200_OK)

    #     return_message = {
    #         'message':FORBIDDEN_MESSAGE
    #     }
    #     return Response(return_message, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, user_id):
        """ Method to delete a single User """
        is_admin = request.user.is_superuser
        validate_admin(is_admin)

        data = get_user_object(user_id)
        data.delete()
        return_message = {
            'message':
            SUCCESS_MESSAGE.format("User has been deleted")
        }
        return Response(return_message, status=status.HTTP_201_CREATED)
