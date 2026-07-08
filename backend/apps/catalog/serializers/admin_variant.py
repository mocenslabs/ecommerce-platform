from rest_framework import serializers

from apps.catalog.models import (
    ProductVariant,
)


class AdminVariantSerializer(
    serializers.ModelSerializer,
):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    class Meta:
        model = ProductVariant

        fields = [
            "id",
            "product",
            "product_name",
            "sku",
            "price",
            "compare_at_price",
            "attributes",
            "is_active",
            "created_at",
        ]
