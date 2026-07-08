import uuid

from django.db import models

from apps.core.models import BaseModel


class Refund(BaseModel):
    """
    Refund associated with a payment.

    Supports:
    - full refunds
    - partial refunds
    - manual refunds
    - provider refunds
    """

    refund_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    payment = models.ForeignKey(
        "payments.Payment",
        on_delete=models.CASCADE,
        related_name="refunds",
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    reason = models.TextField(
        blank=True,
    )

    provider_refund_id = models.CharField(
        max_length=255,
        blank=True,
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
                    "processed",
                ],
            ),
            models.Index(
                fields=[
                    "created_at",
                ],
            ),
        ]

    def __str__(self):
        return str(self.refund_id)
