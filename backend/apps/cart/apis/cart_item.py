from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)

from apps.cart.models import (
    Cart,
    CartItem,
)
from apps.cart.serializers.cart_item import (
    CartItemSerializer,
)
from apps.cart.serializers.cart_item_create import (
    AddCartItemSerializer,
)
from apps.cart.serializers.cart_item_update import (
    CartItemUpdateSerializer,
)
from apps.cart.services.cart import (
    add_item_to_cart,
)
from apps.catalog.models import (
    ProductVariant,
)


class CartItemCreateApi(
    generics.CreateAPIView,
):
    """
    Add item to cart.
    """

    serializer_class = AddCartItemSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(
        self,
        serializer,
    ):
        cart, _ = Cart.objects.get_or_create(
            user=self.request.user,
            checked_out=False,
        )

        variant = get_object_or_404(
            ProductVariant,
            id=serializer.validated_data["variant_id"],
        )

        add_item_to_cart(
            cart=cart,
            variant=variant,
            quantity=serializer.validated_data["quantity"],
        )


class CartItemUpdateApi(
    generics.UpdateAPIView,
):
    """
    Update cart item quantity.
    """

    serializer_class = CartItemUpdateSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(
        self,
    ):
        return CartItem.objects.filter(
            cart__user=self.request.user,
        )


class CartItemDeleteApi(
    generics.DestroyAPIView,
):
    """
    Remove item from cart.
    """

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(
        self,
    ):
        return CartItem.objects.filter(
            cart__user=self.request.user,
        )
