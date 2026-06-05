from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from rest_framework import serializers

from apps.authentication.api.services.auth import (
    generate_tokens_for_user,
    register_user,
)
from apps.users.models import (
    User,
)


class RegisterSerializer(
    serializers.Serializer,
):
    """
    User registration serializer.
    """

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    first_name = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    last_name = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    def validate_email(
        self,
        value,
    ):
        """
        Validate email uniqueness.
        """

        exists = User.objects.filter(
            email=value,
        ).exists()

        if exists:
            raise serializers.ValidationError("Email already exists.")

        return value

    def validate(
        self,
        attrs,
    ):
        """
        Validate registration data.
        """

        django_validate_password(
            attrs["password"],
        )

        return attrs

    def create(
        self,
        validated_data,
    ):
        """
        Create user instance.
        """

        user = register_user(
            **validated_data,
        )

        return user

    def to_representation(
        self,
        instance,
    ):
        """
        Return auth response.
        """

        tokens = generate_tokens_for_user(
            instance,
        )

        return {
            "user": {
                "id": str(instance.id),
                "email": instance.email,
                "first_name": (instance.first_name),
                "last_name": (instance.last_name),
                "role": instance.role,
                "is_verified": (instance.is_verified),
            },
            "tokens": tokens,
        }
