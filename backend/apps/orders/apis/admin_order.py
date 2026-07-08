from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.orders.models import (
    Order,
)
from apps.orders.serializers.admin_order import (
    AdminOrderSerializer,
)


class AdminOrderListApi(
    generics.ListAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = (
        Order.objects.select_related(
            "user",
        )
        .all()
        .order_by(
            "-created_at",
        )
    )

    serializer_class = AdminOrderSerializer


class AdminOrderDetailApi(
    generics.RetrieveUpdateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Order.objects.select_related(
        "user",
    ).all()

    serializer_class = AdminOrderSerializer
