from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from apps.core.permissions.roles import (
    IsAdminUserRole,
)


class AdminTestView(
    APIView,
):
    """
    Test admin-only endpoint.
    """

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(
        self,
        request,
    ):
        """
        Return admin-only response.
        """

        return Response(
            {
                "success": True,
                "message": ("Welcome admin."),
            },
        )
