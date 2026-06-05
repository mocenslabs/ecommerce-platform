from django.urls import path

from apps.payments.apis.webhook import (
    MercadoPagoWebhookApi,
)

urlpatterns = [
    path(
        "webhooks/mercadopago/",
        MercadoPagoWebhookApi.as_view(),
        name="mercadopago-webhook",
    ),
]
