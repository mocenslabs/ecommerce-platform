from django.db import connection
from rest_framework.response import (
    Response,
)
from rest_framework.views import APIView


class ReadinessApi(
    APIView,
):
    """
    Readiness probe endpoint.
    """

    permission_classes = []

    authentication_classes = []

    def get(self, request):
        """
        Validate critical services.
        """

        try:
            connection.cursor()

            return Response(
                {
                    "status": "ready",
                }
            )

        except Exception:
            return Response(
                {
                    "status": "not_ready",
                },
                status=503,
            )
