from rest_framework import serializers

from apps.catalog.models import (
    ProductImage,
)


class ProductImageSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize product images.
    """

    class Meta:
        model = ProductImage

        fields = [
            "id",
            "image",
            "alt_text",
            "is_primary",
            "sort_order",
        ]
