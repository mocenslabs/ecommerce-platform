from rest_framework import serializers

from apps.orders.models import (
    ShippingMethod,
)


class ShippingMethodSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = ShippingMethod

        fields = [
            "id",
            "name",
            "code",
            "price",
            "estimated_days",
        ]
