from rest_framework.permissions import (
    IsAdminUser,
)
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from apps.dashboard.serializers import (
    DashboardStatsSerializer,
    RecentOrderSerializer,
    TopProductSerializer,
)
from apps.dashboard.services.stats import (
    get_dashboard_stats,
    get_recent_orders,
    get_top_products,
)


class DashboardStatsApi(APIView):
    """
    Dashboard overview API.
    """

    permission_classes = [
        IsAdminUser,
    ]

    def get(self, request):
        """
        Return dashboard stats.
        """

        stats = get_dashboard_stats()

        serializer = DashboardStatsSerializer(
            stats,
        )

        return Response(
            serializer.data,
        )


class DashboardTopProductsApi(
    APIView,
):
    """
    Dashboard top products API.
    """

    permission_classes = [
        IsAdminUser,
    ]

    def get(self, request):
        """
        Return top products.
        """

        products = get_top_products()

        serializer = TopProductSerializer(
            products,
            many=True,
        )

        return Response(
            serializer.data,
        )


class DashboardRecentOrdersApi(
    APIView,
):
    """
    Dashboard recent orders API.
    """

    permission_classes = [
        IsAdminUser,
    ]

    def get(self, request):
        """
        Return recent orders.
        """

        orders = get_recent_orders()

        serializer = RecentOrderSerializer(
            orders,
            many=True,
        )

        return Response(
            serializer.data,
        )
