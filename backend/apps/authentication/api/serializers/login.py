from rest_framework import serializers

from apps.authentication.api.services.auth import (
    authenticate_user,
    generate_tokens_for_user,
)


class LoginSerializer(
    serializers.Serializer,
):
    """
    User login serializer.
    """

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
    )

    def validate(
        self,
        attrs,
    ):
        """
        Validate user credentials.
        """

        email = attrs.get(
            "email",
        )

        password = attrs.get(
            "password",
        )

        user = authenticate_user(
            email=email,
            password=password,
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")
        if not user.is_verified:
            raise serializers.ValidationError("Email address is not verified.")

        attrs["user"] = user

        return attrs

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
