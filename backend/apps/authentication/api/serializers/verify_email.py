from rest_framework import serializers

from apps.authentication.api.services.verification import (
    verify_email_token,
)


class VerifyEmailSerializer(
    serializers.Serializer,
):
    """
    Email verification serializer.
    """

    uid = serializers.CharField()

    token = serializers.CharField()

    def validate(
        self,
        attrs,
    ):
        """
        Validate verification token.
        """

        user = verify_email_token(
            uid=attrs["uid"],
            token=attrs["token"],
        )

        if not user:
            raise serializers.ValidationError("Invalid or expired token.")

        attrs["user"] = user

        return attrs
