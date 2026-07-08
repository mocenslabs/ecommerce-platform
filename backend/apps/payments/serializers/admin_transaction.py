from rest_framework import serializers

from apps.payments.models import Transaction


class AdminTransactionSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = Transaction

        fields = (
            "id",
            "transaction_uuid",
            "payment",
            "provider",
            "transaction_id",
            "transaction_type",
            "status",
            "success",
            "request_payload",
            "response_payload",
            "error_message",
            "created_at",
        )
