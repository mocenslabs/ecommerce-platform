from rest_framework import serializers

from apps.catalog.models import (
    ProductImage,
)


class AdminProductImageSerializer(
    serializers.ModelSerializer,
):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    class Meta:
        model = ProductImage

        fields = [
            "id",
            "product",
            "product_name",
            "image",
            "alt_text",
            "is_primary",
            "sort_order",
            "created_at",
        ]


class AdminProductImageCreateUpdateSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = ProductImage

        fields = [
            "product",
            "image",
            "alt_text",
            "is_primary",
            "sort_order",
        ]
