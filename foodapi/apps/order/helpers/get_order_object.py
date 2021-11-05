from django.db.models import Q
from rest_framework.serializers import ValidationError

from ....helpers.serialization_errors import error_dict
from ..models import Order


def get_order_object():
    """
    Function that returns all order items
    """
    menu_obj = Order.objects.filter(status=False)
    return menu_obj


def get_user_order_object(params, user_id):
    """
    Function that returns user's orders
    """

    if params:
        if 'all_orders' in params:
            menu_obj = Order.objects.filter(user_id=user_id)
            return menu_obj
        elif 'pending_orders' in params:
            menu_obj = Order.objects.filter(
                user_id=user_id).filter(status=False)
            return menu_obj
    else:
        raise ValidationError({
            "message": "Kindly pass 'all_orders' or 'pending_orders' in params"
        })
