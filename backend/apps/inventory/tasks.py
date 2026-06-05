from celery import shared_task
from django.utils import timezone

from apps.inventory.models import (
    InventoryReservation,
)
from apps.inventory.services.release import (
    release_inventory_reservations,
)


@shared_task(
    bind=True,
    max_retries=3,
)
def cleanup_expired_reservations(
    self,
):
    """
    Release expired inventory reservations.
    """

    expired_reservations = (
        InventoryReservation.objects.filter(
            expires_at__lt=timezone.now(),
            released=False,
        )
        .select_related("order")
        .distinct()
    )

    processed_orders = set()

    for reservation in expired_reservations:
        order_id = reservation.order.id

        if order_id in processed_orders:
            continue

        release_inventory_reservations(
            reservation.order,
        )

        processed_orders.add(order_id)
