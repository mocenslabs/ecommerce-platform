from rest_framework import serializers

from apps.cart.models import CartItem


class CartItemSerializer(
    serializers.ModelSerializer,
):
    product_name = serializers.CharField(
        source="variant.product.name",
        read_only=True,
    )

    price = serializers.DecimalField(
        source="variant.price",
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )

    subtotal = serializers.SerializerMethodField()

    def get_subtotal(
        self,
        obj,
    ):
        return obj.variant.price * obj.quantity

    class Meta:
        model = CartItem

        fields = [
            "id",
            "variant",
            "product_name",
            "price",
            "quantity",
            "subtotal",
        ]
