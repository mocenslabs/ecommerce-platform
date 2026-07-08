from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.payments.models import WebhookEvent
from apps.payments.serializers.admin_webhook import (
    AdminWebhookSerializer,
)


class AdminWebhookListApi(
    generics.ListAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = WebhookEvent.objects.all().order_by(
        "-created_at",
    )

    serializer_class = AdminWebhookSerializer


class AdminWebhookDetailApi(
    generics.RetrieveAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = WebhookEvent.objects.all()

    serializer_class = AdminWebhookSerializer
