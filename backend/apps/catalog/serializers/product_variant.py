from rest_framework import serializers

from apps.catalog.models import (
    ProductVariant,
)


class ProductVariantSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize product variants.
    """

    class Meta:
        model = ProductVariant

        fields = [
            "id",
            "sku",
            "price",
            "compare_at_price",
            "attributes",
        ]
