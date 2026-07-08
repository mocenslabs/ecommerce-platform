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
    payload,
):
    """
    Handle order paid event.
    """

    order = payload.get(
        "order",
    )

    if not order:
        return

    payment = (
        Payment.objects.filter(
            order=order,
        )
        .order_by(
            "-created_at",
        )
        .first()
    )

    if not payment:
        return

    payment.status = PaymentStatus.PAID

    payment.processed_at = timezone.now()

    payment.save(
        update_fields=[
            "status",
            "processed_at",
        ],
    )

    confirm_inventory_reservations(
        order,
    )

    update_order_status(
        order,
        OrderStatus.PAID,
    )
