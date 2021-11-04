import logging

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.db.models import Q
from django.utils.translation import pgettext_lazy

from ...helpers.push_id import PushID
from ..models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_staff=False,
                    **extra_fields):
        """Create a user instance with the given email and password."""

        email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)

        if password:
            user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):

    ROLES = (
        ('ADMIN', 'admin'),
        ('FOOD_ATTENDANT', 'foo_attendant'),
        ('CUSTOMER_CARE', 'customer_care'),
        ('NORMAL_USER', 'normal_user'),
    )

    role = models.CharField(max_length=50, choices = ROLES, null=True)

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    # role =  models.ForeignKey(Role,  on_delete=models.CASCADE)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case, we want that to be the username field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def save(self, *args, **kwargs):
        push_id = PushID()
        # This to check if it creates a new or updates an old instance
        if not self.id:
            self.id = push_id.next_id()
        super(User, self).save()
    

    class Meta:
        permissions = (
            ("manage_users",
             pgettext_lazy("Permission description", "Manage regular users."),
             ),
            ("manage_staff",
             pgettext_lazy("Permission description", "Manage staff."),
             ),
            ("impersonate_users",
             pgettext_lazy("Permission description", "Impersonate users."),
             ),
        )


    @staticmethod
    def get_user(email):
        try:
            user = User.objects.get(email=email)
            return user

        except Exception:
            return False
