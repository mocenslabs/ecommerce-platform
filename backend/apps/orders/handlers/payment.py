from django.utils import timezone

from apps.inventory.services.confirmation import (
    confirm_inventory_reservations,
)
from apps.orders.constants import (
    OrderStatus,
)
from apps.orders.services.status import (
    update_order_status,
)
from apps.payments.constants import (
    PaymentStatus,
)
from apps.payments.models import (
    Payment,
)


def handle_order_paid(
    event,
):
    """
    Handle order paid event.
    """

    order_id = event.payload.get(
        "order_id",
    )

    if not order_id:
        return

    try:
        payment = Payment.objects.select_related(
            "order",
        ).get(
            order__order_id=order_id,
        )

    except Payment.DoesNotExist:
        return

    payment.status = PaymentStatus.COMPLETED

    payment.processed_at = timezone.now()

    payment.save(
        update_fields=[
            "status",
            "processed_at",
        ],
    )

    confirm_inventory_reservations(
        payment.order,
    )

    update_order_status(
        payment.order,
        OrderStatus.PAID,
    )
