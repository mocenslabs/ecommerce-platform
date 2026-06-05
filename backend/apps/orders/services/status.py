from apps.orders.constants import (
    OrderStatus,
)
from apps.orders.services.events import (
    create_order_event,
)

ALLOWED_TRANSITIONS = {
    OrderStatus.PENDING: [
        OrderStatus.PAID,
        OrderStatus.CANCELLED,
    ],
    OrderStatus.PAID: [
        OrderStatus.PROCESSING,
        OrderStatus.REFUNDED,
    ],
    OrderStatus.PROCESSING: [
        OrderStatus.SHIPPED,
    ],
    OrderStatus.SHIPPED: [
        OrderStatus.DELIVERED,
    ],
}


def can_transition(
    current_status,
    new_status,
):
    """
    Validate order status transition.
    """

    allowed = ALLOWED_TRANSITIONS.get(
        current_status,
        [],
    )

    return new_status in allowed


def update_order_status(
    order,
    new_status,
):
    """
    Safely update order status.
    """

    old_status = order.status

    if not can_transition(
        old_status,
        new_status,
    ):
        raise ValueError(
            f"Invalid transition from {old_status} to {new_status}",
        )

    order.status = new_status

    order.save(
        update_fields=[
            "status",
        ],
    )

    create_order_event(
        order=order,
        event_type="status_changed",
        description=(f"Order status changed from {old_status} to {new_status}"),
        metadata={
            "old_status": old_status,
            "new_status": new_status,
        },
    )

    if new_status == OrderStatus.PAID:
        from apps.core.events.dispatcher import (
            dispatch_event,
        )
        from apps.orders.events import (
            OrderPaidEvent,
        )

        dispatch_event(
            OrderPaidEvent(
                payload={
                    "order_id": str(
                        order.order_id,
                    ),
                },
            ),
        )

    return order
