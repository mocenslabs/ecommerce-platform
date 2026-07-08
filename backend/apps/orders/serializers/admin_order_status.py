from rest_framework import serializers

from apps.orders.constants import (
    OrderStatus,
)


class AdminOrderStatusSerializer(
    serializers.Serializer,
):
    status = serializers.ChoiceField(
        choices=[
            OrderStatus.PROCESSING,
            OrderStatus.SHIPPED,
            OrderStatus.DELIVERED,
            OrderStatus.CANCELLED,
            OrderStatus.REFUNDED,
        ],
    )
