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
    ExpiredReservationSerializer,
    InventoryHealthSerializer,
    LowStockProductSerializer,
    OrdersByStatusSerializer,
    RecentOrderSerializer,
    ReservedInventorySerializer,
    RevenueTrendSerializer,
    TopProductSerializer,
)
from apps.dashboard.services.stats import (
    get_dashboard_stats,
    get_expired_reservations,
    get_inventory_health,
    get_low_stock_products,
    get_orders_by_status,
    get_recent_orders,
    get_reserved_inventory,
    get_revenue_trend,
    get_top_products,
)


class DashboardStatsApi(
    APIView,
):
    """
    Dashboard overview API.
    """

    permission_classes = [
        IsAdminUser,
    ]

    def get(
        self,
        request,
    ):
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

    def get(
        self,
        request,
    ):
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

    def get(
        self,
        request,
    ):
        orders = get_recent_orders()

        serializer = RecentOrderSerializer(
            orders,
            many=True,
        )

        return Response(
            serializer.data,
        )


class DashboardRevenueTrendApi(
    APIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    def get(
        self,
        request,
    ):
        data = get_revenue_trend()

        serializer = RevenueTrendSerializer(
            data,
            many=True,
        )

        return Response(
            serializer.data,
        )


class DashboardOrdersByStatusApi(
    APIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    def get(
        self,
        request,
    ):
        data = get_orders_by_status()

        serializer = OrdersByStatusSerializer(
            data,
            many=True,
        )

        return Response(
            serializer.data,
        )


class DashboardLowStockApi(
    APIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    def get(
        self,
        request,
    ):
        inventory = get_low_stock_products()

        data = [
            {
                "product": (item.variant.product.name),
                "sku": (item.variant.sku),
                "quantity": (item.quantity),
            }
            for item in inventory
        ]

        serializer = LowStockProductSerializer(
            data,
            many=True,
        )

        return Response(
            serializer.data,
        )


class DashboardInventoryHealthApi(
    APIView,
):
    """
    Inventory health dashboard.
    """

    permission_classes = [
        IsAdminUser,
    ]

    def get(
        self,
        request,
    ):
        data = get_inventory_health()

        serializer = InventoryHealthSerializer(
            data,
        )

        return Response(
            serializer.data,
        )


class DashboardReservedInventoryApi(
    APIView,
):
    """
    Reserved inventory dashboard.
    """

    permission_classes = [
        IsAdminUser,
    ]

    def get(
        self,
        request,
    ):
        inventory = get_reserved_inventory()

        data = [
            {
                "product": (item.variant.product.name),
                "sku": (item.variant.sku),
                "quantity": (item.quantity),
                "reserved_quantity": (item.reserved_quantity),
                "available_quantity": (item.available_quantity),
            }
            for item in inventory
        ]

        serializer = ReservedInventorySerializer(
            data,
            many=True,
        )

        return Response(
            serializer.data,
        )


class DashboardExpiredReservationsApi(
    APIView,
):
    """
    Expired reservations dashboard.
    """

    permission_classes = [
        IsAdminUser,
    ]

    def get(
        self,
        request,
    ):
        reservations = get_expired_reservations()

        data = [
            {
                "reservation_id": (item.reservation_id),
                "sku": (item.variant.sku),
                "quantity": (item.quantity),
                "expired_at": (item.updated_at),
            }
            for item in reservations
        ]

        serializer = ExpiredReservationSerializer(
            data,
            many=True,
        )

        return Response(
            serializer.data,
        )
