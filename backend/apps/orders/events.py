class BaseEvent:
    """
    Base domain event.
    """

    def __init__(self, payload):
        self.payload = payload


class OrderCreatedEvent(BaseEvent):
    """
    Fired when order is created.
    """

    pass


class OrderPaidEvent(BaseEvent):
    """
    Fired when order is paid.
    """

    pass


class OrderCancelledEvent(BaseEvent):
    """
    Fired when order is cancelled.
    """

    pass
