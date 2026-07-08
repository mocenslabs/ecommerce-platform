class InventoryMovementType:
    """
    Inventory movement types.
    """

    RESTOCK = "restock"

    RESERVATION = "reservation"

    RELEASE = "release"

    SHIPMENT = "shipment"

    RETURN = "return"

    ADJUSTMENT = "adjustment"

    CHOICES = [
        (RESTOCK, "Restock"),
        (RESERVATION, "Reservation"),
        (RELEASE, "Release"),
        (SHIPMENT, "Shipment"),
        (RETURN, "Return"),
        (ADJUSTMENT, "Adjustment"),
    ]


class InventoryReservationStatus:
    """
    Inventory reservation lifecycle.
    """

    PENDING = "pending"

    ACTIVE = "active"

    CONSUMED = "consumed"

    RELEASED = "released"

    EXPIRED = "expired"

    CHOICES = [
        (PENDING, "Pending"),
        (ACTIVE, "Active"),
        (CONSUMED, "Consumed"),
        (RELEASED, "Released"),
        (EXPIRED, "Expired"),
    ]
