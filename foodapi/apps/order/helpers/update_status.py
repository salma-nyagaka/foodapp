from django.db.models import Q
from rest_framework.serializers import ValidationError

from ..models import Order

def update_status(data, params):
    """
    Function that returns user's orders
    """

    if params:
        if 'accepted' in params:
            data.status = 'Accepted'
            data.save()
            return data
        elif 'declined' in params:
            data.status = 'Declined'
            data.save()
            return data
    else:
        raise ValidationError({
            "message": "Kindly pass 'accepted' or 'declined' in params"
        })