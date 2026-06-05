from apps.notifications.handlers.orders import (
    handle_order_created,
)
from apps.orders.events import (
    OrderCreatedEvent,
    OrderPaidEvent,
)
from apps.orders.handlers.payment import (
    handle_order_paid,
)

EVENT_HANDLERS = {
    OrderPaidEvent: [
        handle_order_paid,
    ],
    OrderCreatedEvent: [
        handle_order_created,
    ],
}


def dispatch_event(
    event,
):
    """
    Dispatch domain event to handlers.
    """

    handlers = EVENT_HANDLERS.get(
        type(event),
        [],
    )

    for handler in handlers:
        handler(
            event.payload,
        )
