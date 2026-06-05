from rest_framework import serializers

from apps.orders.models import (
    Order,
    OrderItem,
)


class OrderItemSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize order items.
    """

    class Meta:
        model = OrderItem

        fields = [
            "id",
            "product_name",
            "sku",
            "quantity",
            "unit_price",
            "total_price",
        ]


class OrderSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize orders with items.
    """

    items = OrderItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Order

        fields = [
            "id",
            "order_number",
            "status",
            "subtotal_amount",
            "shipping_amount",
            "tax_amount",
            "discount_amount",
            "total_amount",
            "created_at",
            "items",
        ]
