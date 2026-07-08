from rest_framework import serializers


class CustomerDashboardSerializer(
    serializers.Serializer,
):
    total_orders = serializers.IntegerField()

    total_spent = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    wishlist_count = serializers.IntegerField()

    address_count = serializers.IntegerField()

    last_order = serializers.SerializerMethodField()

    def get_last_order(
        self,
        obj,
    ):
        order = obj.get(
            "last_order",
        )

        if not order:
            return None

        return {
            "order_number": order.order_number,
            "status": order.status,
            "total_amount": order.total_amount,
            "created_at": order.created_at,
        }
