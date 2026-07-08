from django.conf import settings
from django.db import models

from apps.core.models import BaseModel
from apps.inventory.constants import (
    InventoryMovementType,
)


class InventoryMovement(BaseModel):
    """
    Immutable inventory movement history.

    Every stock change must generate a movement
    record for auditing and traceability.
    """

    variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="inventory_movements",
    )

    movement_type = models.CharField(
        max_length=30,
        choices=InventoryMovementType.CHOICES,
    )

    quantity_change = models.IntegerField()

    reference_type = models.CharField(
        max_length=50,
        blank=True,
    )

    reference_id = models.CharField(
        max_length=100,
        blank=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="inventory_movements",
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

        indexes = [
            models.Index(
                fields=[
                    "movement_type",
                ],
            ),
            models.Index(
                fields=[
                    "created_at",
                ],
            ),
        ]

    def __str__(self):
        return f"{self.variant.sku} | {self.movement_type} | {self.quantity_change}"
