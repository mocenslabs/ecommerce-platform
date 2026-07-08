from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.orders.services.reorder import (
    reorder_order,
)


class ReorderApi(
    APIView,
):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(
        self,
        request,
        order_number,
    ):
        result = reorder_order(
            user=request.user,
            order_number=order_number,
        )

        return Response(
            {
                "detail": "Products added to cart.",
                "cart_id": result["cart"].id,
                "items_added": result["items_added"],
            },
            status=status.HTTP_200_OK,
        )
