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
from apps.authentication.api.serializers.register import (
    RegisterSerializer,
)
from apps.authentication.tasks import (
    send_verification_email,
)


class RegisterView(
    APIView,
):
    """
    Register new user endpoint.
    """

    permission_classes = []

    authentication_classes = []

    def post(
        self,
        request,
    ):
        """
        Register new user.
        """

        serializer = RegisterSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        user = serializer.save()

        send_verification_email.delay(
            str(user.id),
        )

        create_audit_log(
            user=user,
            action="user_registered",
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
            RegisterSerializer(
                user,
            ).data,
            status=(status.HTTP_201_CREATED),
        )
