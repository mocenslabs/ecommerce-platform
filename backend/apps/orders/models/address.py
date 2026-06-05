from django.conf import settings
from django.db import models

from apps.core.models import BaseModel


class Address(BaseModel):
    """
    Customer address used for:
    - shipping
    - billing
    - invoices
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses",
        null=True,
        blank=True,
    )

    first_name = models.CharField(
        max_length=255,
    )

    last_name = models.CharField(
        max_length=255,
    )

    line_1 = models.CharField(
        max_length=255,
    )

    line_2 = models.CharField(
        max_length=255,
        blank=True,
    )

    city = models.CharField(
        max_length=255,
    )

    state = models.CharField(
        max_length=255,
    )

    postal_code = models.CharField(
        max_length=50,
    )

    country = models.CharField(
        max_length=2,
    )

    phone_number = models.CharField(
        max_length=30,
    )

    is_default = models.BooleanField(
        default=False,
    )

    is_billing = models.BooleanField(
        default=False,
    )

    is_shipping = models.BooleanField(
        default=True,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return f"{self.line_1} - {self.city}"
