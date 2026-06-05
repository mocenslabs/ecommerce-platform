class OrderStatus:
    """
    Available order statuses.
    """

    PENDING = "pending"

    PAID = "paid"

    PROCESSING = "processing"

    SHIPPED = "shipped"

    DELIVERED = "delivered"

    CANCELLED = "cancelled"

    REFUNDED = "refunded"

    CHOICES = [
        (PENDING, "Pending"),
        (PAID, "Paid"),
        (PROCESSING, "Processing"),
        (SHIPPED, "Shipped"),
        (DELIVERED, "Delivered"),
        (CANCELLED, "Cancelled"),
        (REFUNDED, "Refunded"),
    ]


class ShippingMethod:
    """
    Available shipping methods.
    """

    STANDARD = "standard"

    EXPRESS = "express"

    PICKUP = "pickup"

    CHOICES = [
        (
            STANDARD,
            "Standard",
        ),
        (
            EXPRESS,
            "Express",
        ),
        (
            PICKUP,
            "Pickup",
        ),
    ]
