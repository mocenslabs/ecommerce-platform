from django.urls import path

from apps.payments.apis.admin import (
    AdminPaymentDetailApi,
    AdminPaymentListApi,
)
from apps.payments.apis.admin_refund import (
    AdminRefundDetailApi,
    AdminRefundListApi,
)
from apps.payments.apis.admin_transaction import (
    AdminTransactionDetailApi,
    AdminTransactionListApi,
)
from apps.payments.apis.admin_webhook import (
    AdminWebhookDetailApi,
    AdminWebhookListApi,
)
from apps.payments.apis.webhook import (
    MercadoPagoWebhookApi,
)

urlpatterns = [
    path(
        "admin/",
        AdminPaymentListApi.as_view(),
        name="admin-payment-list",
    ),
    path(
        "admin/<uuid:pk>/",
        AdminPaymentDetailApi.as_view(),
        name="admin-payment-detail",
    ),
    path(
        "admin/transactions/",
        AdminTransactionListApi.as_view(),
        name="admin-transaction-list",
    ),
    path(
        "admin/transactions/<uuid:pk>/",
        AdminTransactionDetailApi.as_view(),
        name="admin-transaction-detail",
    ),
    path(
        "admin/refunds/",
        AdminRefundListApi.as_view(),
        name="admin-refund-list",
    ),
    path(
        "admin/refunds/<uuid:pk>/",
        AdminRefundDetailApi.as_view(),
        name="admin-refund-detail",
    ),
    path(
        "admin/webhooks/",
        AdminWebhookListApi.as_view(),
        name="admin-webhook-list",
    ),
    path(
        "admin/webhooks/<uuid:pk>/",
        AdminWebhookDetailApi.as_view(),
        name="admin-webhook-detail",
    ),
    path(
        "webhooks/mercadopago/",
        MercadoPagoWebhookApi.as_view(),
        name="mercadopago-webhook",
    ),
]
