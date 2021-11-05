from django.db.models import Q
from rest_framework.serializers import ValidationError

from ....helpers.serialization_errors import error_dict
from ..models import User


def get_user_object(id):
    """
    Function that checks if a specific user  exists
    """
    try:
        user_obj = User.objects.get(id=id)
        return user_obj
    except User.DoesNotExist:
        raise ValidationError({
            "message": error_dict['does_not_exist'].format("User")}
        )
