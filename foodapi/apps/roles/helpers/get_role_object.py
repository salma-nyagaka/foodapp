from rest_framework.serializers import ValidationError

from ....helpers.serialization_errors import error_dict
from ..models import Role


def get_role_object(id):
    """
    Function that checks if a specific role exists
    """
    try:
        role_obj = Role.objects.get(id=id)
        return role_obj
    except Role.DoesNotExist:
        raise ValidationError({
            "message": error_dict['does_not_exist'].format("Role item")}
        )