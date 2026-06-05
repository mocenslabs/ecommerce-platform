from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
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
from apps.authentication.api.serializers.logout import (
    LogoutSerializer,
)


class LogoutView(
    APIView,
):
    """
    Logout authenticated user.
    """

    permission_classes = [
        IsAuthenticated,
    ]

    def post(
        self,
        request,
    ):
        """
        Blacklist refresh token.
        """

        serializer = LogoutSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save()

        create_audit_log(
            user=request.user,
            action="user_logout",
            entity_type="user",
            entity_id=request.user.id,
            metadata={
                "email": request.user.email,
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
                "message": ("Logout successful."),
            },
            status=status.HTTP_200_OK,
        )
