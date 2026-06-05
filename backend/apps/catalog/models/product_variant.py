from django.db import models
from django.db.models import (
    UniqueConstraint,
)

from apps.core.models import BaseModel


class ProductVariant(BaseModel):
    """
    Purchasable product variation.
    """

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="variants",
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    compare_at_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    attributes = models.JSONField(
        default=dict,
        blank=True,
    )

    class Meta:
        ordering = [
            "created_at",
        ]

        indexes = [
            models.Index(
                fields=[
                    "sku",
                ],
            ),
            models.Index(
                fields=[
                    "is_active",
                ],
            ),
            models.Index(
                fields=[
                    "created_at",
                ],
            ),
        ]

        constraints = [
            UniqueConstraint(
                fields=[
                    "product",
                    "sku",
                ],
                name="unique_product_sku",
            ),
        ]

    def __str__(self):
        return f"{self.product.name} - {self.sku}"
