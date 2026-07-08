from rest_framework import serializers

from apps.catalog.models import (
    Product,
)
from apps.orders.models import (
    Order,
)


class DashboardStatsSerializer(
    serializers.Serializer,
):
    """
    Dashboard KPI serializer.
    """

    total_revenue = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    total_orders = serializers.IntegerField()

    paid_orders = serializers.IntegerField()

    pending_orders = serializers.IntegerField()

    cancelled_orders = serializers.IntegerField()

    total_customers = serializers.IntegerField()

    total_products = serializers.IntegerField()


class TopProductSerializer(
    serializers.ModelSerializer,
):
    """
    Best selling product serializer.
    """

    total_sales = serializers.IntegerField()

    class Meta:
        model = Product

        fields = [
            "id",
            "name",
            "slug",
            "total_sales",
            "average_rating",
        ]


class RecentOrderSerializer(
    serializers.ModelSerializer,
):
    """
    Recent order serializer.
    """

    customer = serializers.SerializerMethodField()

    class Meta:
        model = Order

        fields = [
            "id",
            "order_number",
            "status",
            "total_amount",
            "customer",
            "created_at",
        ]

    def get_customer(
        self,
        obj,
    ):
        if not obj.user:
            return None

        return obj.user.email


class RevenueTrendSerializer(
    serializers.Serializer,
):
    month = serializers.DateField()

    revenue = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )


class OrdersByStatusSerializer(
    serializers.Serializer,
):
    status = serializers.CharField()

    total = serializers.IntegerField()


class LowStockProductSerializer(
    serializers.Serializer,
):
    product = serializers.CharField()

    sku = serializers.CharField()

    quantity = serializers.IntegerField()


class InventoryHealthSerializer(
    serializers.Serializer,
):
    """
    Global inventory health metrics.
    """

    total_stock = serializers.IntegerField()

    reserved_stock = serializers.IntegerField()

    available_stock = serializers.IntegerField()

    reserved_percentage = serializers.FloatField()


class ReservedInventorySerializer(
    serializers.Serializer,
):
    """
    Reserved inventory by variant.
    """

    product = serializers.CharField()

    sku = serializers.CharField()

    quantity = serializers.IntegerField()

    reserved_quantity = serializers.IntegerField()

    available_quantity = serializers.IntegerField()


class ExpiredReservationSerializer(
    serializers.Serializer,
):
    """
    Expired reservation serializer.
    """

    reservation_id = serializers.UUIDField()

    sku = serializers.CharField()

    quantity = serializers.IntegerField()

    expired_at = serializers.DateTimeField()
