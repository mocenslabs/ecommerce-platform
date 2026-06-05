from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cart.models import Cart
from apps.core.throttling import (
    CheckoutRateThrottle,
)
from apps.orders.exceptions.checkout import (
    EmptyCartException,
    InsufficientStockException,
    InvalidQuantityException,
)
from apps.orders.models import (
    Address,
    ShippingMethod,
)
from apps.orders.serializers.checkout import (
    CheckoutSerializer,
)
from apps.orders.services.checkout import (
    process_checkout,
)


class CheckoutApi(APIView):
    """
    API endpoint responsible for
    authenticated checkout.
    """

    permission_classes = [IsAuthenticated]

    throttle_classes = [
        CheckoutRateThrottle,
    ]

    def post(self, request):
        """
        Process authenticated checkout.
        """

        serializer = CheckoutSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        data = serializer.validated_data

        try:
            cart = Cart.objects.get(
                user=request.user,
            )

        except Cart.DoesNotExist:
            return Response(
                {
                    "detail": "Cart not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        shipping_address = Address.objects.get(
            id=data["shipping_address_id"],
        )

        billing_address = None

        if data.get(
            "billing_address_id",
        ):
            billing_address = Address.objects.get(
                id=data["billing_address_id"],
            )

        shipping_method = ShippingMethod.objects.get(
            id=data["shipping_method_id"],
        )

        try:
            order = process_checkout(
                user=request.user,
                cart=cart,
                shipping_address=(shipping_address),
                billing_address=(billing_address),
                shipping_method=(shipping_method),
                discount_code=data.get(
                    "discount_code",
                ),
            )

        except EmptyCartException as error:
            return Response(
                {
                    "detail": str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except InvalidQuantityException as error:
            return Response(
                {
                    "detail": str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except InsufficientStockException as error:
            return Response(
                {
                    "detail": str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "order_id": str(order.order_number),
                "status": order.status,
                "subtotal": str(order.subtotal_amount),
                "shipping": str(order.shipping_amount),
                "tax": str(order.tax_amount),
                "total": str(order.total_amount),
            },
            status=status.HTTP_201_CREATED,
        )
