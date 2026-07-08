from rest_framework import status
from rest_framework.permissions import (
    IsAdminUser,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.orders.models import (
    Order,
)
from apps.orders.serializers.admin_order_status import (
    AdminOrderStatusSerializer,
)
from apps.orders.services.status import (
    update_order_status,
)


class AdminOrderStatusApi(
    APIView,
):
    """
    Update order status from admin/staff panel.
    """

    permission_classes = [
        IsAdminUser,
    ]

    def post(
        self,
        request,
        order_number,
    ):
        serializer = AdminOrderStatusSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        try:
            order = Order.objects.get(
                order_number=order_number,
            )

        except Order.DoesNotExist:
            return Response(
                {
                    "detail": "Order not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            update_order_status(
                order,
                serializer.validated_data["status"],
            )

        except ValueError as exc:
            return Response(
                {
                    "detail": str(exc),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "order_number": str(
                    order.order_number,
                ),
                "status": order.status,
            },
            status=status.HTTP_200_OK,
        )
