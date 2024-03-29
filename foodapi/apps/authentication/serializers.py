from django.contrib.auth import authenticate
from rest_framework import serializers, validators
from rest_framework.fields import USE_READONLYFIELD
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator

from foodapi.helpers.validate_user import validate_admin
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    def __init__(self, *args, **kwargs):
        super(RegistrationSerializer, self).__init__(*args, **kwargs)

        # Override the default error_messages with a custom field error
        for field in self.fields:
            error_messages = self.fields[field].error_messages
            error_messages['null'] = error_messages['blank'] \
                = error_messages['required'] \
                = 'Please fill in the {}.'.format(field)

    email = serializers.RegexField(
        regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",
        validators=[
            validators.UniqueValidator(
                queryset=User.objects.all(),
                message='Email address already exists',
            )
        ],
    )

    # Ensure that username is unique, does not exist,
    #  cannot be left be blank, has a minimum of 5 characters
    # has alphanumerics only
    username = serializers.RegexField(
        regex='^[A-Za-z\-\_]+\d*$',
        min_length=4,
        max_length=30,
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='The username already exists. Kindly try another.'
        )],
        error_messages={
            'min_length': 'Username must have a minimum of 4 characters.',
            'max_length': 'Username must have a maximum of 30 characters.',
            'invalid': 'Username cannot only have alphanumeric characters.'
        }
    )

    # Ensure passwords are at least 8 characters long,
    password = serializers.RegexField(
        regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
        max_length=128,
        write_only=True,
        error_messages={
            'max_length': 'Password cannot be more than 128 characters',
            'invalid': 'Password must have a minimum of '
                       'eight characters at least one letter'
                       ' and one number'
        }
    )
    # token = serializers.SerializerMethodField()

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'username', 'password', 'role']

    def create(self, validated_data):
        if 'role' in validated_data:
            if validated_data['role'] == 'ADMIN':
                user = User.objects.create_user(
                    **validated_data, is_superuser=True)
            else:
                user = User.objects.create_user(**validated_data)
        else:
            raise ValidationError({
                "role": "Please fill in the role."
            })

        return user


class LoginSerializer(serializers.Serializer):
    """The class to serialize login details"""
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        """
        The `validate` method is where we make sure that the current
        instance of `LoginSerializer` has "valid". In the case of logging a
        user in, this means validating that they've provided an email
        and password and that this combination matches one of the users in
        our database.
        """
        email = data.get('email', None)
        password = data.get('password', None)

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value. Remember that, in our User
        # model, we set `USERNAME_FIELD` as `username`.
        user = authenticate(email=email, password=password)

        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'Either your email or password is not right.'
                'Kindly double check them'
            )

        """
        The `validate` method should return a dictionary of validated data.
        This is the data that is passed to the `create` and `update` methods
        that we will see later on.
        """
        return {
            'email': user.email,
            'username': user.username
        }


class UserSerializer(serializers.ModelSerializer):
    """ Serialize user's data"""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
