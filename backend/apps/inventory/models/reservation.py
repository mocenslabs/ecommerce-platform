import uuid

from django.db import models

from apps.core.models import BaseModel
from apps.inventory.constants import (
    InventoryReservationStatus,
)


class InventoryReservation(BaseModel):
    """
    Temporary inventory reservation.

    Reservations are created during checkout to prevent
    overselling while the customer completes payment.

    Lifecycle:

    ACTIVE
        Reservation currently holding stock.

    CONSUMED
        Reservation converted into a completed sale.

    RELEASED
        Reservation manually released.

    EXPIRED
        Reservation automatically expired.

    PENDING
        Reservation created but not yet activated.
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

    quantity = models.PositiveIntegerField(
        help_text=("Reserved quantity for this reservation."),
    )

    expires_at = models.DateTimeField(
        help_text=("Reservation expiration timestamp."),
    )

    status = models.CharField(
        max_length=20,
        choices=(InventoryReservationStatus.CHOICES),
        default=(InventoryReservationStatus.ACTIVE),
        help_text=("Current reservation lifecycle state."),
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
                    "status",
                ],
            ),
            models.Index(
                fields=[
                    "created_at",
                ],
            ),
        ]

    def __str__(self):
        """
        Human readable representation.

        Returns:
            str
        """

        return f"{self.variant.sku} - {self.quantity} ({self.status})"
