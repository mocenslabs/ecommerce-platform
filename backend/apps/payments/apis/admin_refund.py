from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.payments.models import Refund
from apps.payments.serializers.admin_refund import (
    AdminRefundSerializer,
)


class AdminRefundListApi(
    generics.ListAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = (
        Refund.objects.select_related(
            "payment",
        )
        .all()
        .order_by(
            "-created_at",
        )
    )

    serializer_class = AdminRefundSerializer


class AdminRefundDetailApi(
    generics.RetrieveAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Refund.objects.select_related(
        "payment",
    ).all()

    serializer_class = AdminRefundSerializer
