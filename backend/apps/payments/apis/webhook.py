from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.throttling import (
    WebhookRateThrottle,
)
from apps.payments.services.webhook import (
    process_mercadopago_webhook,
)


class MercadoPagoWebhookApi(
    APIView,
):
    """
    MercadoPago webhook endpoint.
    """

    authentication_classes = []
    permission_classes = []

    throttle_classes = [
        WebhookRateThrottle,
    ]

    def post(
        self,
        request,
    ):
        """
        Process MercadoPago webhook.
        """

        process_mercadopago_webhook(
            request.data,
        )

        return Response(
            {
                "detail": "Webhook received",
            },
            status=status.HTTP_200_OK,
        )
