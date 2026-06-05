from apps.orders.models import (
    OrderEvent,
)


def create_order_event(
    order,
    event_type,
    description="",
    metadata=None,
):
    """
    Create order timeline event.
    """

    return OrderEvent.objects.create(
        order=order,
        event_type=event_type,
        description=description,
        metadata=metadata or {},
    )
