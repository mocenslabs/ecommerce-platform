from rest_framework import status
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from apps.audit.services import (
    create_audit_log,
)
from apps.authentication.api.serializers.login import (
    LoginSerializer,
)


class LoginView(
    APIView,
):
    """
    User login endpoint.
    """

    permission_classes = []

    authentication_classes = []

    def post(
        self,
        request,
    ):
        """
        Authenticate user.
        """

        serializer = LoginSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        user = serializer.validated_data["user"]

        create_audit_log(
            user=user,
            action="user_login",
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
            LoginSerializer(
                user,
            ).data,
            status=(status.HTTP_200_OK),
        )
