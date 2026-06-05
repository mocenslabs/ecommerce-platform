import uuid

from django.db import models

from apps.core.models import BaseModel
from apps.payments.constants import (
    PaymentProvider,
    PaymentStatus,
)


class Payment(BaseModel):
    """
    Represents a payment attempt associated with an order.

    A single order may have multiple payment attempts due to:
    - retries
    - failed payments
    - provider issues
    - recovery flows
    """

    payment_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="payments",
    )

    provider = models.CharField(
        max_length=50,
        choices=PaymentProvider.CHOICES,
    )

    status = models.CharField(
        max_length=30,
        choices=PaymentStatus.CHOICES,
        default=PaymentStatus.PENDING,
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    external_id = models.CharField(
        max_length=255,
        blank=True,
    )

    idempotency_key = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    raw_response = models.JSONField(
        default=dict,
        blank=True,
    )

    processed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "status",
                ],
            ),
            models.Index(
                fields=[
                    "provider",
                ],
            ),
            models.Index(
                fields=[
                    "external_id",
                ],
            ),
            models.Index(
                fields=[
                    "created_at",
                ],
            ),
        ]

    def __str__(self):
        return str(self.payment_id)
