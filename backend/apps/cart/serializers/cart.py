from rest_framework import serializers

from apps.cart.models import Cart
from apps.cart.serializers.cart_item import (
    CartItemSerializer,
)
from apps.cart.services.totals import (
    calculate_cart_subtotal,
)


class CartSerializer(
    serializers.ModelSerializer,
):
    items = CartItemSerializer(
        many=True,
        read_only=True,
    )

    subtotal = serializers.SerializerMethodField()

    def get_subtotal(
        self,
        obj,
    ):
        return calculate_cart_subtotal(
            obj,
        )

    class Meta:
        model = Cart

        fields = [
            "id",
            "session_key",
            "items",
            "subtotal",
        ]
