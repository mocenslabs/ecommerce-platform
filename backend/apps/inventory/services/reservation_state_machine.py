from apps.inventory.constants import (
    InventoryReservationStatus,
)
from apps.inventory.models import (
    InventoryReservation,
)


class InvalidReservationTransition(
    Exception,
):
    """
    Invalid reservation state transition.
    """


ALLOWED_TRANSITIONS = {
    InventoryReservationStatus.ACTIVE: [
        InventoryReservationStatus.CONSUMED,
        InventoryReservationStatus.RELEASED,
        InventoryReservationStatus.EXPIRED,
    ],
    InventoryReservationStatus.CONSUMED: [],
    InventoryReservationStatus.RELEASED: [],
    InventoryReservationStatus.EXPIRED: [],
    InventoryReservationStatus.PENDING: [
        InventoryReservationStatus.ACTIVE,
    ],
}


def transition_reservation(
    reservation: InventoryReservation,
    new_status: str,
):
    """
    Perform reservation state transition.

    Args:
        reservation:
            InventoryReservation instance.

        new_status:
            Target state.

    Raises:
        InvalidReservationTransition

    Returns:
        InventoryReservation
    """

    current_status = reservation.status

    allowed = ALLOWED_TRANSITIONS.get(
        current_status,
        [],
    )

    if new_status not in allowed:
        raise InvalidReservationTransition(
            (f"Cannot transition {current_status} to {new_status}")
        )

    reservation.status = new_status

    reservation.save(
        update_fields=[
            "status",
        ],
    )

    return reservation
