from django.db.models import Q
from rest_framework.serializers import ValidationError

from ..helpers.serialization_errors import error_dict


def validate_admin(user):
    """
    Function that checks if a user is an admin
    """
    if user is not True:
        raise ValidationError({
            "message": error_dict['not_allowed']}
        )


def validate_attendant(user):
    """
    Function that checks if a user is a food attendant
    """
    if user is 'NORMAL_USER':
        raise ValidationError({
            "message": error_dict['not_allowed']}
        )


def validate_attendant_or_admin(user):
    """
    Function that checks if a user is an admin or food attendant
    """
    # import pdb
    # pdb.set_trace()
    if user is 'NORMAL_USER':
        raise ValidationError({
            "message": error_dict['not_allowed']}
        )
