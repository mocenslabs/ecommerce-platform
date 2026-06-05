import uuid

from django.db import models

from apps.core.models import BaseModel


class WebhookEvent(
    BaseModel,
):
    """
    Stores processed webhook events.

    Prevents duplicate webhook processing.
    """

    webhook_event_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    provider = models.CharField(
        max_length=50,
    )

    external_event_id = models.CharField(
        max_length=255,
        unique=True,
    )

    event_type = models.CharField(
        max_length=100,
    )

    payload = models.JSONField(
        default=dict,
    )

    processed = models.BooleanField(
        default=False,
    )

    processed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "external_event_id",
                ],
            ),
            models.Index(
                fields=[
                    "processed",
                ],
            ),
            models.Index(
                fields=[
                    "created_at",
                ],
            ),
        ]

    def __str__(
        self,
    ):
        return f"{self.provider} - {self.external_event_id}"
