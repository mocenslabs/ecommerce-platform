from rest_framework import serializers

from apps.payments.models import Refund


class AdminRefundSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = Refund

        fields = (
            "id",
            "refund_id",
            "payment",
            "amount",
            "reason",
            "provider_refund_id",
            "processed",
            "processed_at",
            "created_at",
        )
