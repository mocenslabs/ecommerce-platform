from django.db import transaction

from apps.audit.services import create_audit_log
from apps.core.events.dispatcher import dispatch_event
from apps.inventory.services.release import release_inventory_reservations
from apps.orders.constants import OrderStatus
from apps.orders.events import OrderCancelledEvent
from apps.orders.services.events import (
    create_order_event,
)


class OrderCannotBeCancelled(Exception):
    pass


@transaction.atomic
def cancel_order(order, user):
    """
    Cancel an order safely.

    Rules:
    - Only PENDING orders can be cancelled
    - Releases inventory reservations
    - Marks order as CANCELLED
    - Emits event
    - Writes audit log
    """

    if order.status != OrderStatus.PENDING:
        raise OrderCannotBeCancelled("Only pending orders can be cancelled.")

    # Release inventory
    release_inventory_reservations(order)

    # Update order status
    order.status = OrderStatus.CANCELLED
    order.save(update_fields=["status"])

    create_order_event(
        order=order,
        event_type="order_cancelled",
        description="Order cancelled by customer.",
        metadata={
            "user_id": user.id,
        },
    )

    # Audit log
    create_audit_log(
        user=user,
        action="order_cancelled",
        entity_type="order",
        entity_id=order.id,
        metadata={
            "order_number": str(order.order_number),
        },
    )

    # Event
    dispatch_event(
        OrderCancelledEvent(
            payload={
                "order_id": order.id,
                "status": order.status,
            }
        )
    )

    return order
