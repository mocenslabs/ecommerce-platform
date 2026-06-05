class NotificationType:
    """
    Available notification types.
    """

    ORDER_CREATED = "order_created"

    ORDER_PAID = "order_paid"

    ORDER_SHIPPED = "order_shipped"

    ORDER_DELIVERED = "order_delivered"

    PAYMENT_FAILED = "payment_failed"

    LOW_STOCK = "low_stock"

    CHOICES = [
        (
            ORDER_CREATED,
            "Order Created",
        ),
        (
            ORDER_PAID,
            "Order Paid",
        ),
        (
            ORDER_SHIPPED,
            "Order Shipped",
        ),
        (
            ORDER_DELIVERED,
            "Order Delivered",
        ),
        (
            PAYMENT_FAILED,
            "Payment Failed",
        ),
        (
            LOW_STOCK,
            "Low Stock",
        ),
    ]
