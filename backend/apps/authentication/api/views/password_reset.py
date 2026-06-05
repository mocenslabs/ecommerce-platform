from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from apps.audit.services import (
    create_audit_log,
)
from apps.authentication.api.serializers.password_reset import (
    PasswordResetConfirmSerializer,
    PasswordResetRequestSerializer,
)
from apps.users.models import (
    User,
)


class PasswordResetRequestView(
    APIView,
):
    """
    Request password reset email.
    """

    permission_classes = [
        AllowAny,
    ]

    authentication_classes = []

    def post(
        self,
        request,
    ):
        """
        Send password reset email.
        """

        serializer = PasswordResetRequestSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save()

        user = User.objects.get(email=serializer.validated_data["email"])

        create_audit_log(
            user=user,
            action="password_reset_requested",
            entity_type="user",
            entity_id=user.id,
            metadata={
                "email": user.email,
            },
            ip_address=request.META.get(
                "REMOTE_ADDR",
            ),
            user_agent=request.META.get(
                "HTTP_USER_AGENT",
                "",
            ),
        )

        return Response(
            {
                "success": True,
                "message": ("Password reset email sent."),
            },
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(
    APIView,
):
    """
    Confirm password reset.
    """

    permission_classes = [
        AllowAny,
    ]

    authentication_classes = []

    def post(
        self,
        request,
    ):
        """
        Reset user password.
        """

        serializer = PasswordResetConfirmSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        user = serializer.save()

        create_audit_log(
            user=user,
            action="password_reset_completed",
            entity_type="user",
            entity_id=user.id,
            metadata={
                "email": user.email,
            },
            ip_address=request.META.get(
                "REMOTE_ADDR",
            ),
            user_agent=request.META.get(
                "HTTP_USER_AGENT",
                "",
            ),
        )

        return Response(
            {
                "success": True,
                "message": ("Password updated successfully."),
            },
            status=status.HTTP_200_OK,
        )
