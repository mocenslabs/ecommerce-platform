from django.utils import timezone

from apps.audit.services import (
    create_audit_log,
)
from apps.core.events.dispatcher import (
    dispatch_event,
)
from apps.core.logging import (
    logger,
)
from apps.orders.events import (
    OrderPaidEvent,
)
from apps.orders.models import (
    Order,
)
from apps.payments.models import (
    WebhookEvent,
)


def process_mercadopago_webhook(
    payload,
):
    """
    Process MercadoPago webhook payload.
    """

    external_event_id = payload.get(
        "id",
    )

    event_type = payload.get(
        "type",
    )

    if not external_event_id:
        return

    webhook_event, created = WebhookEvent.objects.get_or_create(
        external_event_id=external_event_id,
        defaults={
            "provider": "mercadopago",
            "event_type": event_type,
            "payload": payload,
        },
    )

    if not created:
        return

    if event_type != "payment":
        return

    data = payload.get(
        "data",
        {},
    )

    order_id = data.get(
        "order_id",
    )

    if not order_id:
        return

    order = (
        Order.objects.select_for_update()
        .filter(
            id=order_id,
        )
        .first()
    )

    if not order:
        return

    try:
        order = Order.objects.get(
            id=order_id,
        )

    except Order.DoesNotExist:
        logger.error((f"Order not found {order_id}"))

    return

    dispatch_event(
        OrderPaidEvent(
            payload={
                "order": order,
            },
        ),
    )

    webhook_event.processed = True

    logger.info((f"Webhook processed {external_event_id}"))

    create_audit_log(
        action="payment_webhook_processed",
        entity_type="payment",
        entity_id=external_event_id,
        metadata={
            "provider": "mercadopago",
            "event_type": event_type,
        },
    )

    webhook_event.processed_at = timezone.now()

    webhook_event.save(
        update_fields=[
            "processed",
            "processed_at",
        ],
    )
