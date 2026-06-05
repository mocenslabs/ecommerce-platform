from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)

from apps.orders.models import Order
from apps.orders.serializers.order import (
    OrderSerializer,
)


class OrderListApi(
    generics.ListAPIView,
):
    """
    Return authenticated user orders.
    """

    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return user orders.
        """

        return (
            Order.objects.filter(
                user=self.request.user,
            )
            .prefetch_related(
                "items",
            )
            .order_by(
                "-created_at",
            )
        )


class OrderDetailApi(
    generics.RetrieveAPIView,
):
    """
    Return single order detail.
    """

    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    lookup_field = "order_number"

    def get_queryset(self):
        """
        Return authenticated user orders.
        """

        return Order.objects.filter(
            user=self.request.user,
        ).prefetch_related(
            "items",
        )
