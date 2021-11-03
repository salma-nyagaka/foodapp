from rest_framework import serializers
from .models import Role
from rest_framework.validators import UniqueValidator


class RoleSerializer(serializers.ModelSerializer):
    """ Serializer data when creating role """

    title = serializers.RegexField(
        regex="[-~]*$",
        required=True,
        validators=[UniqueValidator(
            queryset=Role.objects.all(),
            message='The role titile already exists. Kindly try another.'
        )],
    )

    class Meta:
        model = Role
        fields = [
            'title'
        ]

class SingleRoleSerializer(serializers.ModelSerializer):
    """ Serializer data when accessing a single role """

    class Meta:
        model = Role
        fields = ('__all__')
