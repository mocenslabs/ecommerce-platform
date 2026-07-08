from rest_framework import serializers

from apps.payments.models import WebhookEvent


class AdminWebhookSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = WebhookEvent

        fields = (
            "id",
            "webhook_event_id",
            "provider",
            "external_event_id",
            "event_type",
            "processed",
            "processed_at",
            "created_at",
        )
