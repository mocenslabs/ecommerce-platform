from rest_framework import serializers
from rest_framework_simplejwt.exceptions import (
    TokenError,
)
from rest_framework_simplejwt.tokens import (
    RefreshToken,
)


class LogoutSerializer(
    serializers.Serializer,
):
    """
    Logout serializer.
    """

    refresh = serializers.CharField()

    def save(
        self,
        **kwargs,
    ):
        """
        Blacklist refresh token.
        """

        refresh_token = self.validated_data["refresh"]

        try:
            token = RefreshToken(
                refresh_token,
            )

            token.blacklist()

        except TokenError:
            raise serializers.ValidationError(
                {"refresh": ("Invalid or expired token.")}
            )
