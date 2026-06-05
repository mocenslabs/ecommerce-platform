from django.db import transaction

from apps.inventory.models import (
    Inventory,
)


@transaction.atomic
def release_inventory_reservations(
    order,
):
    """
    Release all inventory reservations
    associated with an order.
    """

    reservations = order.inventory_reservations.select_related(
        "variant",
    ).filter(
        released=False,
    )

    for reservation in reservations:
        inventory = Inventory.objects.select_for_update().get(
            variant=reservation.variant,
        )

        inventory.reserved_quantity -= reservation.quantity

        inventory.save()

        reservation.released = True

        reservation.save(
            update_fields=[
                "released",
            ],
        )
