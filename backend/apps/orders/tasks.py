from celery import shared_task
from django.db import transaction

from apps.audit.services import (
    create_audit_log,
)
from apps.core.logging import (
    logger,
)
from apps.core.tasks import (
    BaseTaskWithRetry,
)
from apps.inventory.models import (
    InventoryReservation,
)
from apps.inventory.services.reservation_lifecycle import (
    consume_reservation,
)
from apps.orders.constants import (
    OrderStatus,
)
from apps.orders.models import (
    Order,
)


@shared_task(
    bind=True,
    base=BaseTaskWithRetry,
)
def send_order_confirmation_email(
    self,
    order_id,
):
    """
    Send confirmation email asynchronously.

    Args:
        order_id:
            Order UUID.
    """

    order = Order.objects.get(
        id=order_id,
    )

    print((f"Sending confirmation email for order {order.id}"))


@shared_task(
    bind=True,
    base=BaseTaskWithRetry,
)
def handle_order_paid_event(
    self,
    payload,
):
    """
    Process paid order workflow.

    Responsibilities:
    - mark order as paid
    - consume inventory reservations
    - create audit log
    - send confirmation email

    Args:
        payload:
            Event payload.
    """

    order = payload.get(
        "order",
    )

    if not order:
        logger.error("OrderPaidEvent without order.")
        return

    with transaction.atomic():
        order.status = OrderStatus.PAID

        order.save(
            update_fields=[
                "status",
            ],
        )

        reservations = InventoryReservation.objects.filter(
            order=order,
            status="active",
        )

        for reservation in reservations:
            consume_reservation(
                reservation,
            )

        create_audit_log(
            user=order.user,
            action="order_paid",
            entity_type="order",
            entity_id=order.id,
            metadata={
                "order_number": str(
                    order.order_number,
                ),
            },
        )

    send_order_confirmation_email.delay(
        str(order.id),
    )

    logger.info((f"Order paid workflow completed {order.id}"))
