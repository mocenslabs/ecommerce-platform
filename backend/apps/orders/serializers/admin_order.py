from rest_framework import serializers

from apps.orders.models import (
    Order,
)


class AdminOrderSerializer(
    serializers.ModelSerializer,
):
    customer_email = serializers.SerializerMethodField()

    def get_customer_email(
        self,
        obj,
    ):
        """
        Return customer email.

        Use authenticated user email
        when available, otherwise
        fallback to guest checkout email.
        """

        if obj.user:
            return obj.user.email

        return obj.email

    class Meta:
        model = Order

        fields = [
            "id",
            "order_number",
            "customer_email",
            "status",
            "subtotal_amount",
            "shipping_amount",
            "tax_amount",
            "discount_amount",
            "total_amount",
            "created_at",
        ]
