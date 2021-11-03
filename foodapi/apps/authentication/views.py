import os
from django.shortcuts import redirect
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ...helpers.constants import SUCCESS_MESSAGE, FORBIDDEN_MESSAGE
from ...helpers.renderers import RequestJSONRenderer
from .models import User
from .serializers import LoginSerializer, RegistrationSerializer
from .backends import JWTAuthentication

class RoleAPIView(GenericAPIView):
    """Register a new user with a role"""
    # permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        """ Signup a new user """
        is_admin = request.user.is_superuser
        # if is_admin:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if serializer.is_valid():
            return_message = {
                'message':
                SUCCESS_MESSAGE.format("Your account has been created"),
                "data": serializer.data
            }
            return Response(return_message, status=status.HTTP_201_CREATED)
        return_message = {
            'message': serializer.errors
        }
        return Response(return_message, status=status.HTTP_400_BAD_REQUEST)
    # return_message = {
    #     'message':FORBIDDEN_MESSAGE
    # }
    # return Response(return_message, status=status.HTTP_403_FORBIDDEN)


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
        user_data['token'] = JWTAuthentication.generate_token(userdata=userdata)

        return_message = {
            'message':SUCCESS_MESSAGE.format("You have logged in"),
            "data": user_data,
            "token": user_data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)
