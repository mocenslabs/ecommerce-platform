from django.db import transaction
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


@transaction.atomic
def process_mercadopago_webhook(
    payload,
):
    """
    Process MercadoPago webhook payload.

    Responsibilities:
    - deduplicate webhook events
    - validate payload
    - locate related order
    - dispatch domain events
    - create audit trail
    - mark webhook as processed

    Args:
        payload:
            MercadoPago webhook payload.

    Returns:
        None
    """

    external_event_id = payload.get(
        "id",
    )

    event_type = payload.get(
        "type",
    )

    if not external_event_id:
        logger.warning("Webhook received without id.")
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
        logger.info((f"Duplicate webhook ignored {external_event_id}"))
        return

    if event_type != "payment":
        logger.info((f"Ignoring webhook event {event_type}"))
        return

    data = payload.get(
        "data",
        {},
    )

    order_id = data.get(
        "order_id",
    )

    if not order_id:
        logger.warning(("Payment webhook received without order_id."))
        return

    try:
        order = Order.objects.select_for_update().get(
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

    webhook_event.processed_at = timezone.now()

    webhook_event.save(
        update_fields=[
            "processed",
            "processed_at",
        ],
    )

    create_audit_log(
        action="payment_webhook_processed",
        entity_type="payment",
        entity_id=external_event_id,
        metadata={
            "provider": "mercadopago",
            "event_type": event_type,
            "order_id": str(
                order.id,
            ),
        },
    )

    logger.info((f"Webhook processed {external_event_id}"))
