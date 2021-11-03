from django.db import models

from ...helpers.push_id import PushID
from ..models import BaseModel


class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    ADMIN = 1
    FOOD_ATTENDANT = 2
    CUSTOMER_CARE = 3
    NORMAL_USER = 4
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (FOOD_ATTENDANT, 'food_attendant'),
        (CUSTOMER_CARE, 'customer_care'),
        (NORMAL_USER, 'normal_user'),
    )

    role= models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
    id = models.CharField(db_index=True, max_length=255,
                            unique=True)


    def save(self, *args, **kwargs):
        push_id = PushID()
        # This to check if it creates a new or updates an old instance
        if not self.id:
            self.id = push_id.next_id()
        super(Role, self).save()
    def __str__(self):
        return self.role()