from rest_framework import serializers

from apps.orders.models import (
    ShippingMethod,
)


class AdminShippingMethodSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = ShippingMethod

        fields = (
            "id",
            "name",
            "code",
            "price",
            "active",
            "estimated_days",
            "free_shipping_threshold",
            "created_at",
        )
