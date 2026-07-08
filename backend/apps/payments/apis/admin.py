from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.payments.models import (
    Payment,
)
from apps.payments.serializers.admin_payment import (
    AdminPaymentSerializer,
)


class AdminPaymentListApi(
    generics.ListAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = (
        Payment.objects.select_related(
            "order",
        )
        .all()
        .order_by(
            "-created_at",
        )
    )

    serializer_class = AdminPaymentSerializer


class AdminPaymentDetailApi(
    generics.RetrieveAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Payment.objects.select_related(
        "order",
    ).all()

    serializer_class = AdminPaymentSerializer
