import uuid

from django.db import models

from apps.core.models import BaseModel


class Transaction(
    BaseModel,
):
    """
    Immutable payment transaction log.

    Stores provider communication history for:
    - auditing
    - debugging
    - dispute analysis
    - webhook tracking
    """

    transaction_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    payment = models.ForeignKey(
        "payments.Payment",
        on_delete=models.CASCADE,
        related_name="transactions",
    )

    provider = models.CharField(
        max_length=50,
    )

    transaction_id = models.CharField(
        max_length=255,
    )

    transaction_type = models.CharField(
        max_length=100,
    )

    status = models.CharField(
        max_length=50,
    )

    success = models.BooleanField(
        default=False,
    )

    request_payload = models.JSONField(
        default=dict,
        blank=True,
    )

    response_payload = models.JSONField(
        default=dict,
        blank=True,
    )

    raw_payload = models.JSONField(
        default=dict,
    )

    error_message = models.TextField(
        blank=True,
    )

    def __str__(
        self,
    ):
        return self.transaction_id
