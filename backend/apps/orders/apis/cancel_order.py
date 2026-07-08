from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.orders.models import Order
from apps.orders.services.cancel_order import OrderCannotBeCancelled, cancel_order


class CancelOrderApi(APIView):
    """
    Cancel order endpoint.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, order_number):
        try:
            order = Order.objects.get(
                order_number=order_number,
                user=request.user,
            )

        except Order.DoesNotExist:
            return Response(
                {"detail": "Order not found."},
                status=404,
            )

        try:
            order = cancel_order(order, request.user)

        except OrderCannotBeCancelled as e:
            return Response(
                {"detail": str(e)},
                status=400,
            )

        return Response(
            {
                "order_number": str(order.order_number),
                "status": order.status,
            },
            status=200,
        )
