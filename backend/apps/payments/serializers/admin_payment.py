from rest_framework import serializers

from apps.payments.models import Payment


class AdminPaymentSerializer(serializers.ModelSerializer):
    order_number = serializers.SerializerMethodField()

    class Meta:
        model = Payment

        fields = (
            "id",
            "order",
            "order_number",
            "provider",
            "status",
            "amount",
            "external_id",
            "created_at",
        )

    def get_order_number(
        self,
        obj,
    ):
        if not obj.order:
            return None

        return str(obj.order.order_number)
