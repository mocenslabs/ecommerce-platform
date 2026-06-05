from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.audit.services import (
    create_audit_log,
)
from apps.authentication.api.serializers.user import (
    UserSerializer,
)
from apps.authentication.api.serializers.verify_email import (
    VerifyEmailSerializer,
)


class VerifyEmailApi(APIView):
    """
    Verify user email endpoint.
    """

    permission_classes = []

    authentication_classes = []

    def post(
        self,
        request,
    ):
        """
        Verify email token.
        """

        serializer = VerifyEmailSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        user = serializer.validated_data["user"]

        user.verify_email()

        create_audit_log(
            user=user,
            action="email_verified",
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
                "message": ("Email verified successfully."),
                "user": (
                    UserSerializer(
                        user,
                    ).data
                ),
            },
            status=status.HTTP_200_OK,
        )
