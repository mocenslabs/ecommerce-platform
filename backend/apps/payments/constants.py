class PaymentStatus:
    PENDING = "pending"
    PROCESSING = "processing"
    AUTHORIZED = "authorized"
    PAID = "paid"
    FAILED = "failed"
    REFUNDED = "refunded"
    CANCELLED = "cancelled"

    CHOICES = [
        (PENDING, "Pending"),
        (PROCESSING, "Processing"),
        (AUTHORIZED, "Authorized"),
        (PAID, "Paid"),
        (FAILED, "Failed"),
        (REFUNDED, "Refunded"),
        (CANCELLED, "Cancelled"),
    ]


class PaymentProvider:
    STRIPE = "stripe"
    MERCADOPAGO = "mercadopago"

    CHOICES = [
        (STRIPE, "Stripe"),
        (MERCADOPAGO, "MercadoPago"),
    ]
