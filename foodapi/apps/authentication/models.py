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
        if username is None:
            raise TypeError('Users must have a username.')


        if email is None:
            raise TypeError('Users must have an email address.')

        email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)

        if password:
            user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser rights.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    ADMIN = 'admin'
    CUSTOMER_CARE = 'customer_care'
    FOOD_ATTENDANT = 'food_attendant'
    
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CUSTOMER_CARE, 'Customer Care'),
        (FOOD_ATTENDANT, 'Food attendant'),
    )

    username = models.CharField(db_index=True, max_length=255, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    email = models.EmailField(db_index=True, unique=True)

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

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.email


    @staticmethod
    def get_user(email):
        try:
            user = User.objects.get(email=email)
            return user

        except Exception:
            return False

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = User.objects.get(id=user_id)
            return user

        except Exception:
            return False