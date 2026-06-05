from django.db import models

from apps.core.models import BaseModel


class ShippingMethod(BaseModel):
    """
    Dynamic shipping methods.
    """

    name = models.CharField(
        max_length=255,
    )

    code = models.CharField(
        max_length=100,
        unique=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    active = models.BooleanField(
        default=True,
    )

    estimated_days = models.PositiveIntegerField(
        default=3,
    )

    free_shipping_threshold = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
