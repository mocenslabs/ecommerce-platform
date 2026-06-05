from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from apps.inventory.models import (
    Inventory,
    InventoryReservation,
)


@transaction.atomic
def reserve_inventory_for_order(order):
    """
    Reserve inventory units for all order items.

    This operation runs atomically to prevent
    race conditions and overselling scenarios.

    Args:
        order: Order instance.

    Raises:
        ValueError: If insufficient inventory exists.

    Returns:
        list[InventoryReservation]
    """
    reservations = []

    for item in order.items.select_related(
        "variant",
    ):
        inventory = Inventory.objects.select_for_update().get(
            variant=item.variant,
        )

        if inventory.available_quantity < item.quantity:
            raise ValueError("Insufficient inventory.")

        inventory.reserved_quantity += item.quantity

        inventory.save()

        reservation = InventoryReservation.objects.create(
            order=order,
            variant=item.variant,
            quantity=item.quantity,
            expires_at=(timezone.now() + timedelta(minutes=15)),
        )

        reservations.append(reservation)

    return reservations
