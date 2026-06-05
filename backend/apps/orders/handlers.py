from apps.orders.tasks import (
    handle_order_paid_event,
)


def handle_order_paid_email(event):
    """
    Send async order paid processing.
    """

    handle_order_paid_event.delay(
        event.payload,
    )
