from django.conf import settings
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)


class HealthCheckApi(
    APIView,
):
    """
    Liveness health check.
    """

    permission_classes = []

    authentication_classes = []

    def get(
        self,
        request,
    ):
        """
        Return service status.
        """

        return Response(
            {
                "status": "healthy",
                "environment": (settings.ENVIRONMENT),
            }
        )
