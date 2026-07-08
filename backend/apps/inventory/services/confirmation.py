from django.db import transaction

from apps.inventory.constants import (
    InventoryReservationStatus,
)
from apps.inventory.services.reservation_lifecycle import (
    consume_reservation,
)


@transaction.atomic
def confirm_inventory_reservations(
    order,
):
    """
    Confirm inventory reservations
    after successful payment.
    """

    reservations = order.inventory_reservations.filter(
        status=InventoryReservationStatus.ACTIVE,
    )

    for reservation in reservations:
        consume_reservation(
            reservation,
        )
