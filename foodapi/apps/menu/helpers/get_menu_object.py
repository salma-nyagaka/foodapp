from django.db.models import Q
from rest_framework.serializers import ValidationError

from ....helpers.serialization_errors import error_dict
from ..models import Menu


def get_menu_object(id):
    """
    Function that checks if a specific menu item exists
    """
    try:
        menu_obj = Menu.objects.get(id=id)
        return menu_obj
    except Menu.DoesNotExist:
        raise ValidationError({
            "message": error_dict['does_not_exist'].format("Menu item")}
        )
