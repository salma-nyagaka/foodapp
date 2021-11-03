from django.db.models import Q
from rest_framework.serializers import ValidationError

from ....helpers.serialization_errors import error_dict
from ..models import Order


def get_order_object(params):
    """
    Function that checks if a specific order item exists
    """
    if params:
        try:
            menu_obj = Order.objects.get(id=id)
            return menu_obj
        except Order.DoesNotExist:
            raise ValidationError({
                "message": error_dict['does_not_exist'].format("Order item")}
            )


def get_user_order_object(params, user_id):
    """
    Function that returns user's orders
    """

    try:
        if 'all_orders' in params:
            menu_obj = Order.objects.filter(user_id=user_id)
            return menu_obj
        elif 'pending_orders' in params:
            menu_obj = Order.objects.filter(
                user_id=user_id).filter(status=False)
            return menu_obj
    except Exception as e:
        raise ValidationError({
            "message": e
        })
