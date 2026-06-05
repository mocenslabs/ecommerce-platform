from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from apps.authentication.api.serializers.user import (
    UserSerializer,
)


class MeView(
    APIView,
):
    """
    Return authenticated user.
    """

    permission_classes = [
        IsAuthenticated,
    ]

    def get(
        self,
        request,
    ):
        """
        Return current user.
        """

        serializer = UserSerializer(
            request.user,
        )

        return Response(
            serializer.data,
        )
