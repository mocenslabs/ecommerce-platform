from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from apps.users.serializers.dashboard import (
    CustomerDashboardSerializer,
)
from apps.users.services.dashboard import (
    get_customer_dashboard,
)


class CustomerDashboardApi(
    APIView,
):
    """
    Customer dashboard.
    """

    permission_classes = [
        IsAuthenticated,
    ]

    def get(
        self,
        request,
    ):
        data = get_customer_dashboard(
            request.user,
        )

        serializer = CustomerDashboardSerializer(
            data,
        )

        return Response(
            serializer.data,
        )
