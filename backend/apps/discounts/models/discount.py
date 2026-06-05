import uuid

from django.db import models

from apps.core.models import BaseModel
from apps.discounts.constants import (
    DiscountType,
)


class Discount(BaseModel):
    """
    Flexible discount / coupon model.
    """

    discount_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        unique=True,
    )

    discount_type = models.CharField(
        max_length=20,
        choices=DiscountType.CHOICES,
    )

    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    minimum_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    usage_limit = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    used_count = models.PositiveIntegerField(
        default=0,
    )

    active = models.BooleanField(
        default=True,
    )

    starts_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    expires_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.code
