from celery import shared_task
from django.utils import timezone

from apps.core.logging import (
    logger,
)
from apps.inventory.constants import (
    InventoryReservationStatus,
)
from apps.inventory.models import (
    InventoryReservation,
)
from apps.inventory.services.reservation_lifecycle import (
    expire_reservation,
)


@shared_task(
    bind=True,
    max_retries=3,
)
def cleanup_expired_reservations(
    self,
):
    """
    Expire active reservations that exceeded
    their expiration timestamp.

    This task runs periodically through
    Celery Beat.

    Expiration flow:

    ACTIVE
        ↓
    EXPIRED
        ↓
    Inventory restored
        ↓
    RELEASE movement created
    """

    reservations = InventoryReservation.objects.filter(
        status=(InventoryReservationStatus.ACTIVE),
        expires_at__lt=timezone.now(),
    ).select_related(
        "variant",
        "order",
    )

    processed = 0

    for reservation in reservations:
        expire_reservation(
            reservation,
        )

        processed += 1

    logger.info((f"Expired reservations processed: {processed}"))

    return processed
