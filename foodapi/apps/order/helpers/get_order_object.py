from django.db.models import Q
from rest_framework.serializers import ValidationError

from ....helpers.serialization_errors import error_dict
from ..models import Order


def get_order_object(id):
    """
    Function that checks if a specific order item exists
    """
    try:
        menu_obj = Order.objects.get(id=id)
        return menu_obj
    except Order.DoesNotExist:
        raise ValidationError({
            "message": error_dict['does_not_exist'].format("Order item")}
        )
