
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from ...helpers.constants import SUCCESS_MESSAGE, NOT_FOUND, FORBIDDEN_MESSAGE
from ...helpers.renderers import RequestJSONRenderer
from .helpers.get_role_object import get_role_object
from .serializers import RoleSerializer, SingleRoleSerializer
from .models import Role


class RoleAPIView(generics.GenericAPIView):
    """ Class to create a role """
    renderer_classes = (RequestJSONRenderer, )

    def post(self, request):
        """ Function to create a new role"""

        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.is_valid():
            return_message = {
                'message': SUCCESS_MESSAGE.format("Role has been created"),
                "data": serializer.data
            }
            return Response(return_message, status=status.HTTP_201_CREATED)
        return_message = {
            'error': serializer.errors
        }
        return Response(return_message, status=status.HTTP_400_BAD_REQUEST)


class AllRolesPIView(generics.RetrieveAPIView):
    """ Class to get all roles"""
    serializer_class = SingleRoleSerializer

    def get(self, request):
        """ Method to get all roles """

        data = Role.objects.all()
        serializer = self.serializer_class(data, many=True)

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("All roles have been fetched"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)


class SingleRoleAPIView(generics.RetrieveAPIView):
    """ Class to get, update, delete a single role item"""
    serializer_class = SingleRoleSerializer

    def get(self, request, role_id):
        """ Method to get a single role"""
        data = get_role_object(role_id)
        serializer = self.serializer_class(data)

        return_message = {
            'message':
            SUCCESS_MESSAGE.format("Role has been fetched"),
            "data": serializer.data
        }
        return Response(return_message, status=status.HTTP_201_CREATED)

    def put(self, request, role_id):
        """ Method to update a single role"""
        question_obj = get_role_object(role_id)
        serializer = self.serializer_class(
            question_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return_message = {
                'message': SUCCESS_MESSAGE.format("The rolehas been updated"),
                "data": serializer.data
            }
            return Response(return_message, status=status.HTTP_200_OK)
        return_message = {
            'message': serializer.errors
        }
        return Response(return_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, role_id):
        """ Method to delete a single role"""
        data = Role.objects.get(id=role_id)
        data.delete()
        return_message = {
            'message':
            SUCCESS_MESSAGE.format("Role has has been deleted")
        }
        return Response(return_message, status=status.HTTP_201_CREATED)
