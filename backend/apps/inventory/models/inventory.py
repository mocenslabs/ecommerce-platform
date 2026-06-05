from django.db import models

from apps.core.models import BaseModel


class Inventory(BaseModel):
    """
    Tracks sellable inventory for a product variant.

    Inventory reservations are handled separately through
    reserved_quantity to prevent overselling during checkout.
    """

    variant = models.OneToOneField(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="inventory",
    )

    quantity = models.PositiveIntegerField(
        default=0,
    )

    reserved_quantity = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        verbose_name_plural = "Inventory"

        indexes = [
            models.Index(
                fields=[
                    "created_at",
                ],
            ),
        ]

    @property
    def available_quantity(self) -> int:
        """
        Calculate currently available inventory.

        Returns:
            int: Available stock excluding reserved units.
        """
        return self.quantity - self.reserved_quantity

    def __str__(self):
        return f"{self.variant.sku} - {self.quantity}"
