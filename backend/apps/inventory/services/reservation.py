from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from apps.inventory.constants import (
    InventoryMovementType,
)
from apps.inventory.models import (
    Inventory,
    InventoryReservation,
)
from apps.inventory.services.movement import (
    create_inventory_movement,
)


@transaction.atomic
def reserve_inventory_for_order(
    order,
):
    """
    Reserve inventory for all order items.

    This operation locks inventory rows to prevent
    concurrent stock modifications and overselling.

    For every successful reservation an inventory
    movement record is created for traceability.

    Args:
        order:
            Order instance.

    Raises:
        ValueError:
            If insufficient inventory exists.

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

        inventory.save(
            update_fields=[
                "reserved_quantity",
            ],
        )

        reservation = InventoryReservation.objects.create(
            order=order,
            variant=item.variant,
            quantity=item.quantity,
            expires_at=(
                timezone.now()
                + timedelta(
                    minutes=15,
                )
            ),
        )

        create_inventory_movement(
            variant=item.variant,
            movement_type=(InventoryMovementType.RESERVATION),
            quantity_change=(-item.quantity),
            reference_type="reservation",
            reference_id=(reservation.reservation_id),
            notes=("Inventory reserved during checkout."),
        )

        reservations.append(
            reservation,
        )

    return reservations
