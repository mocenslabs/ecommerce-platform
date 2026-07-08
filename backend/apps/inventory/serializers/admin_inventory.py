from rest_framework import serializers

from apps.inventory.models import (
    Inventory,
)


class AdminInventorySerializer(
    serializers.ModelSerializer,
):
    sku = serializers.CharField(
        source="variant.sku",
        read_only=True,
    )

    available_quantity = serializers.IntegerField(
        read_only=True,
    )

    class Meta:
        model = Inventory

        fields = [
            "id",
            "variant",
            "sku",
            "quantity",
            "reserved_quantity",
            "available_quantity",
            "created_at",
        ]
