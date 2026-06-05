from django.db import transaction

from apps.inventory.models import (
    Inventory,
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
        confirmed=False,
    )

    for reservation in reservations:
        inventory = Inventory.objects.select_for_update().get(
            variant=reservation.variant,
        )

        inventory.reserved_quantity -= reservation.quantity

        inventory.quantity -= reservation.quantity

        inventory.save()

        reservation.confirmed = True

        reservation.save(
            update_fields=[
                "confirmed",
            ],
        )
