from django.db import transaction

from apps.inventory.constants import (
    InventoryMovementType,
    InventoryReservationStatus,
)
from apps.inventory.models import (
    Inventory,
)
from apps.inventory.services.movement import (
    create_inventory_movement,
)
from apps.inventory.services.reservation_state_machine import (
    transition_reservation,
)


def _validate_reserved_quantity(
    inventory,
    reservation,
):
    """
    Validate inventory consistency.

    Prevents negative reserved inventory caused by
    corrupted data, manual DB modifications or
    unexpected state transitions.

    Args:
        inventory:
            Inventory instance.

        reservation:
            InventoryReservation instance.

    Raises:
        ValueError:
            If reserved stock is inconsistent.
    """

    if inventory.reserved_quantity < reservation.quantity:
        raise ValueError(
            (
                "Inventory inconsistency detected. "
                "Reserved quantity is lower than "
                "reservation quantity."
            )
        )


@transaction.atomic
def release_reservation(
    reservation,
):
    """
    Release reserved inventory.

    Used when:
    - order cancelled
    - payment failed
    - manual release
    """

    inventory = Inventory.objects.select_for_update().get(
        variant=reservation.variant,
    )

    _validate_reserved_quantity(
        inventory,
        reservation,
    )

    inventory.reserved_quantity -= reservation.quantity

    inventory.save(
        update_fields=[
            "reserved_quantity",
        ],
    )

    transition_reservation(
        reservation,
        InventoryReservationStatus.RELEASED,
    )

    create_inventory_movement(
        variant=reservation.variant,
        movement_type=(InventoryMovementType.RELEASE),
        quantity_change=(reservation.quantity),
        reference_type="reservation",
        reference_id=(reservation.reservation_id),
        notes=("Reservation released."),
    )

    return reservation


@transaction.atomic
def expire_reservation(
    reservation,
):
    """
    Expire reservation and restore stock.
    """

    inventory = Inventory.objects.select_for_update().get(
        variant=reservation.variant,
    )

    _validate_reserved_quantity(
        inventory,
        reservation,
    )

    inventory.reserved_quantity -= reservation.quantity

    inventory.save(
        update_fields=[
            "reserved_quantity",
        ],
    )

    transition_reservation(
        reservation,
        InventoryReservationStatus.EXPIRED,
    )

    create_inventory_movement(
        variant=reservation.variant,
        movement_type=(InventoryMovementType.RELEASE),
        quantity_change=(reservation.quantity),
        reference_type="reservation",
        reference_id=(reservation.reservation_id),
        notes=("Reservation expired."),
    )

    return reservation


@transaction.atomic
def consume_reservation(
    reservation,
):
    """
    Consume reservation after successful payment.

    Converts reserved inventory into sold inventory.

    State:

    ACTIVE -> CONSUMED
    """

    inventory = Inventory.objects.select_for_update().get(
        variant=reservation.variant,
    )

    _validate_reserved_quantity(
        inventory,
        reservation,
    )

    inventory.quantity -= reservation.quantity

    inventory.reserved_quantity -= reservation.quantity

    inventory.save(
        update_fields=[
            "quantity",
            "reserved_quantity",
        ],
    )

    transition_reservation(
        reservation,
        InventoryReservationStatus.CONSUMED,
    )

    create_inventory_movement(
        variant=reservation.variant,
        movement_type=(InventoryMovementType.SHIPMENT),
        quantity_change=(-reservation.quantity),
        reference_type="reservation",
        reference_id=(reservation.reservation_id),
        notes=("Reservation consumed after successful payment."),
    )

    return reservation
