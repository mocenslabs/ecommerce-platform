from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from rest_framework import serializers

from apps.authentication.api.services.password_reset import (
    validate_password_reset_token,
)
from apps.authentication.tasks import (
    send_password_reset_email,
)
from apps.users.models import (
    User,
)


class PasswordResetRequestSerializer(
    serializers.Serializer,
):
    """
    Password reset request serializer.
    """

    email = serializers.EmailField()

    def validate_email(
        self,
        value,
    ):
        """
        Validate user email exists.
        """

        user_exists = User.objects.filter(
            email=value,
        ).exists()

        if not user_exists:
            raise serializers.ValidationError("User with this email does not exist.")

        return value

    def save(
        self,
        **kwargs,
    ):
        """
        Send password reset email.
        """

        user = User.objects.get(email=self.validated_data["email"])

        send_password_reset_email.delay(
            str(user.id),
        )


class PasswordResetConfirmSerializer(
    serializers.Serializer,
):
    """
    Password reset confirmation serializer.
    """

    uid = serializers.CharField()

    token = serializers.CharField()

    password = serializers.CharField(
        min_length=8,
        write_only=True,
    )

    def validate(
        self,
        attrs,
    ):
        """
        Validate password reset token
        and password strength.
        """

        user = validate_password_reset_token(
            uid=attrs["uid"],
            token=attrs["token"],
        )

        if not user:
            raise serializers.ValidationError("Invalid or expired token.")

        django_validate_password(
            attrs["password"],
            user=user,
        )

        attrs["user"] = user

        return attrs

    def save(
        self,
        **kwargs,
    ):
        """
        Update user password.
        """

        user = self.validated_data["user"]

        password = self.validated_data["password"]

        user.set_password(
            password,
        )

        user.save(
            update_fields=[
                "password",
            ]
        )

        return user
