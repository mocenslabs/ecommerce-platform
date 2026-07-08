from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)

from apps.cart.models import Cart
from apps.cart.serializers.cart import (
    CartSerializer,
)


class CartDetailApi(
    generics.RetrieveAPIView,
):
    """
    Return authenticated user cart.
    """

    serializer_class = CartSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(
        self,
    ):
        cart, _ = Cart.objects.get_or_create(
            user=self.request.user,
            checked_out=False,
        )

        return cart
