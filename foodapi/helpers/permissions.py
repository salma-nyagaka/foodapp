from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission
from ..apps.authentication.models import User
from ..apps.roles.models import Role
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .constants import SUCCESS_MESSAGE

class PermissionsApiView(generics.GenericAPIView):
    # new_group, created = Group.objects.get_or_create(name='new_group')
    # ct = ContentType.objects.get_for_model(Logs)

    # permission = Permission.objects.create(codename='can_clean_logs',
    #                                 name='Can clean logs',
    #                                 content_type=ct)
    # new_group.permissions.add(permission)
    # user_type = ContentType.objects.get(app_label='User', model='User')
    def get(self, request):
        user_content_type = ContentType.objects.get_for_model(User)
        all_user_permissions = Permission.objects.filter(content_type=user_content_type)
        roles_content_type = ContentType.objects.get_for_model(Role)
        all_roles_permissions = Permission.objects.filter(content_type=roles_content_type)
        return_message = {
            'message':SUCCESS_MESSAGE.format("You have fetched all the permissions")
        }
        return Response(return_message, status=status.HTTP_201_CREATED)
