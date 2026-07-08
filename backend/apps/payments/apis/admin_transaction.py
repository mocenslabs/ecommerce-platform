from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.payments.models import Transaction
from apps.payments.serializers.admin_transaction import (
    AdminTransactionSerializer,
)


class AdminTransactionListApi(
    generics.ListAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = (
        Transaction.objects.select_related(
            "payment",
        )
        .all()
        .order_by(
            "-created_at",
        )
    )

    serializer_class = AdminTransactionSerializer


class AdminTransactionDetailApi(
    generics.RetrieveAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Transaction.objects.select_related(
        "payment",
    ).all()

    serializer_class = AdminTransactionSerializer
