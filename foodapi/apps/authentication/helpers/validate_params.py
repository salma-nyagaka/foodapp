from django.db.models import Q
from rest_framework.serializers import ValidationError

from ....helpers.serialization_errors import error_dict


def validate_parans(params):
    """
    Function that checks if admin is in params
    """

    if params:
        if 'is_admin' not in params:
            raise ValidationError({
                "message": error_dict['not_allowed']}
            )
    else:
        raise ValidationError({
            "message": error_dict['not_allowed']}
        )
