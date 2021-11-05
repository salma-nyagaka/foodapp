from django.db.models import Q
from rest_framework.serializers import ValidationError

from ..helpers.serialization_errors import error_dict


def validate_admin(user):
    """
    Function that checks if a user is an admin
    """
    if user != True:
        raise ValidationError({
            "message": error_dict['not_allowed']}
        )


def validate_attendant(user):
    """
    Function that checks if a user is a food attendant
    """
    if user != 'FOOD_ATTENDANT':
        raise ValidationError({
            "message": error_dict['not_allowed']}
        )


def validate_attendant_or_admin(user):
    """
    Function that checks if a user is an admin or food attendant
    """
    if user != 'FOOD_ATTENDANT' or 'ADMIN':
        raise ValidationError({
            "message": error_dict['not_allowed']}
        )
