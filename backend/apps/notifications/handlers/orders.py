from apps.notifications.constants import (
    NotificationType,
)
from apps.notifications.services.notification import (
    create_notification,
)
from apps.notifications.tasks import (
    send_order_created_email_task,
    send_order_paid_email_task,
)


def handle_order_paid(
    payload,
):
    """
    Handle order paid event.
    """

    order = payload["order"]

    if not order.user:
        return

    create_notification(
        user=order.user,
        notification_type=(NotificationType.ORDER_PAID),
        title="Payment received",
        message=(f"Your order {order.order_number} has been paid successfully."),
        data={
            "order_id": str(order.id),
        },
    )

    send_order_paid_email_task.delay(
        order.id,
    )


def handle_order_created(
    payload,
):
    """
    Handle order created event.
    """

    order = payload["order"]

    if not order.user:
        return

    create_notification(
        user=order.user,
        notification_type=(NotificationType.ORDER_CREATED),
        title="Order created",
        message=(f"Your order {order.order_number} was created successfully."),
        data={
            "order_id": str(order.id),
        },
    )

    send_order_created_email_task.delay(
        order.id,
    )
