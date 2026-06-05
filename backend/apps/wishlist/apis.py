from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalog.models import Product
from apps.wishlist.models import (
    WishlistItem,
)
from apps.wishlist.serializers import (
    WishlistItemSerializer,
)
from apps.wishlist.services import (
    add_product_to_wishlist,
    get_or_create_wishlist,
    remove_product_from_wishlist,
)


class WishlistApi(APIView):
    """
    Manage customer wishlist.
    """

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        """
        Return wishlist items.
        """

        wishlist = get_or_create_wishlist(
            request.user,
        )

        items = (
            WishlistItem.objects.select_related(
                "product",
            )
            .prefetch_related(
                "product__images",
            )
            .filter(
                wishlist=wishlist,
            )
        )

        serializer = WishlistItemSerializer(
            items,
            many=True,
        )

        return Response(
            serializer.data,
        )

    def post(self, request):
        """
        Add product to wishlist.
        """

        product = get_object_or_404(
            Product,
            id=request.data["product_id"],
            is_active=True,
        )

        item = add_product_to_wishlist(
            request.user,
            product,
        )

        serializer = WishlistItemSerializer(
            item,
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request):
        """
        Remove product from wishlist.
        """

        product = get_object_or_404(
            Product,
            id=request.data["product_id"],
        )

        remove_product_from_wishlist(
            request.user,
            product,
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
