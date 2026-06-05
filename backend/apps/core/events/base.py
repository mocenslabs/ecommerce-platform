class DomainEvent:
    """
    Base domain event.
    """

    event_name = "domain.event"

    def __init__(
        self,
        payload=None,
    ):
        self.payload = payload or {}
