from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.orders.constants import OrderStatus
from apps.orders.models import Order
from apps.orders.services.status import (
    update_order_status,
)


class BaseAdminStatusApi(APIView):
    permission_classes = [
        IsAdminUser,
    ]

    target_status = None

    def post(
        self,
        request,
        order_number,
    ):
        try:
            order = Order.objects.get(
                order_number=order_number,
            )

        except Order.DoesNotExist:
            return Response(
                {
                    "detail": "Order not found.",
                },
                status=404,
            )

        try:
            update_order_status(
                order,
                self.target_status,
            )

        except ValueError as error:
            return Response(
                {
                    "detail": str(error),
                },
                status=400,
            )

        return Response(
            {
                "order_number": str(order.order_number),
                "status": order.status,
            },
            status=200,
        )


class AdminOrderProcessingApi(
    BaseAdminStatusApi,
):
    target_status = OrderStatus.PROCESSING


class AdminOrderShippedApi(
    BaseAdminStatusApi,
):
    target_status = OrderStatus.SHIPPED


class AdminOrderDeliveredApi(
    BaseAdminStatusApi,
):
    target_status = OrderStatus.DELIVERED


class AdminOrderRefundApi(
    BaseAdminStatusApi,
):
    target_status = OrderStatus.REFUNDED
