import uuid

from django.db import models

from apps.core.models import BaseModel


class InventoryReservation(BaseModel):
    """
    Temporary inventory reservation during checkout flow.

    Reservations help prevent overselling while users
    complete payment processing.
    """

    reservation_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="inventory_reservations",
    )

    variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="reservations",
    )

    quantity = models.PositiveIntegerField()

    expires_at = models.DateTimeField()

    released = models.BooleanField(
        default=False,
    )

    confirmed = models.BooleanField(
        default=False,
    )

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "expires_at",
                ],
            ),
            models.Index(
                fields=[
                    "released",
                ],
            ),
            models.Index(
                fields=[
                    "created_at",
                ],
            ),
        ]

    def __str__(self):
        return f"{self.variant.sku} - {self.quantity}"
