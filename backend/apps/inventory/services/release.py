from django.db import transaction

from apps.inventory.constants import (
    InventoryReservationStatus,
)
from apps.inventory.services.reservation_lifecycle import (
    release_reservation,
)


@transaction.atomic
def release_inventory_reservations(
    order,
):
    """
    Release all active inventory reservations
    associated with an order.
    """

    reservations = order.inventory_reservations.filter(
        status=InventoryReservationStatus.ACTIVE,
    )

    for reservation in reservations:
        release_reservation(
            reservation,
        )
