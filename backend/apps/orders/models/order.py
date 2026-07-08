import uuid

from django.conf import settings
from django.db import models

from apps.core.models import BaseModel
from apps.discounts.models import (
    Discount,
)
from apps.orders.constants import (
    OrderStatus,
)
from apps.orders.models.shipping_method import (
    ShippingMethod,
)


class Order(BaseModel):
    order_number = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="orders",
    )

    email = models.EmailField()

    status = models.CharField(
        max_length=30,
        choices=OrderStatus.CHOICES,
        default=OrderStatus.PENDING,
    )

    billing_address = models.ForeignKey(
        "orders.Address",
        on_delete=models.PROTECT,
        related_name="billing_orders",
    )

    shipping_address = models.ForeignKey(
        "orders.Address",
        on_delete=models.PROTECT,
        related_name="shipping_orders",
    )

    # ==========================================
    # Billing Snapshot
    # ==========================================

    billing_first_name = models.CharField(
        max_length=255,
        blank=True,
    )

    billing_last_name = models.CharField(
        max_length=255,
        blank=True,
    )

    billing_phone = models.CharField(
        max_length=30,
        blank=True,
    )

    billing_line_1 = models.CharField(
        max_length=255,
        blank=True,
    )

    billing_line_2 = models.CharField(
        max_length=255,
        blank=True,
    )

    billing_city = models.CharField(
        max_length=255,
        blank=True,
    )

    billing_state = models.CharField(
        max_length=255,
        blank=True,
    )

    billing_postal_code = models.CharField(
        max_length=50,
        blank=True,
    )

    billing_country = models.CharField(
        max_length=2,
        blank=True,
    )

    # ==========================================
    # Shipping Snapshot
    # ==========================================

    shipping_first_name = models.CharField(
        max_length=255,
        blank=True,
    )

    shipping_last_name = models.CharField(
        max_length=255,
        blank=True,
    )

    shipping_phone = models.CharField(
        max_length=30,
        blank=True,
    )

    shipping_line_1 = models.CharField(
        max_length=255,
        blank=True,
    )

    shipping_line_2 = models.CharField(
        max_length=255,
        blank=True,
    )

    shipping_city = models.CharField(
        max_length=255,
        blank=True,
    )

    shipping_state = models.CharField(
        max_length=255,
        blank=True,
    )

    shipping_postal_code = models.CharField(
        max_length=50,
        blank=True,
    )

    shipping_country = models.CharField(
        max_length=2,
        blank=True,
    )

    subtotal_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    shipping_method = models.ForeignKey(
        ShippingMethod,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    shipping_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    discount = models.ForeignKey(
        Discount,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    discount_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    tax_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    checked_out_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

        indexes = [
            models.Index(
                fields=[
                    "status",
                ],
            ),
            models.Index(
                fields=[
                    "created_at",
                ],
            ),
        ]

    def __str__(self):
        return str(self.order_number)
