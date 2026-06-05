from rest_framework import serializers

from apps.catalog.serializers.product import (
    ProductListSerializer,
)
from apps.wishlist.models import (
    WishlistItem,
)


class WishlistItemSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize wishlist item.
    """

    product = ProductListSerializer(
        read_only=True,
    )

    class Meta:
        model = WishlistItem

        fields = [
            "id",
            "product",
            "created_at",
        ]
