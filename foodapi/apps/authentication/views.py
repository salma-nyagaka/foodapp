import os
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ...helpers.constants import SUCCESS_MESSAGE
from ...helpers.renderers import RequestJSONRenderer
from .models import User
from .serializers import LoginSerializer, RegistrationSerializer
from .backends import JWTAuthentication

class RegistrationAPIView(GenericAPIView):
    """Register a new user"""
    permission_classes = (AllowAny,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request, **kwargs):
        """ Signup a new user """
        serializer = self.serializer_class(data=request.data)
        import pdb
        pdb.set_trace()
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
