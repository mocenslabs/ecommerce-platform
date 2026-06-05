from decimal import Decimal

from django.db import transaction

from apps.audit.services import (
    create_audit_log,
)
from apps.core.events.dispatcher import (
    dispatch_event,
)
from apps.core.logging import (
    logger,
)
from apps.discounts.models import (
    Discount,
)
from apps.discounts.services.calculator import (
    calculate_discount_amount,
)
from apps.discounts.services.validation import (
    validate_discount,
)
from apps.inventory.models import (
    Inventory,
)
from apps.inventory.services.reservation import (
    reserve_inventory_for_order,
)
from apps.orders.constants import (
    OrderStatus,
)
from apps.orders.events import (
    OrderCreatedEvent,
)
from apps.orders.exceptions.checkout import (
    EmptyCartException,
    InsufficientStockException,
    InvalidQuantityException,
)
from apps.orders.models import (
    Order,
    OrderItem,
)
from apps.orders.services.shipping.service import (
    calculate_shipping_for_order,
)
from apps.orders.services.tax.service import (
    calculate_tax_for_order,
)
from apps.orders.tasks import (
    send_order_confirmation_email,
)
from apps.payments.services.payment import (
    create_payment_for_order,
)


@transaction.atomic
def process_checkout(
    user,
    cart,
    shipping_address,
    shipping_method,
    billing_address=None,
    discount_code=None,
):
    """
    Process complete checkout flow.

    Responsibilities:
    - validate cart
    - validate inventory
    - create order
    - create order items
    - reserve inventory
    - create payment
    - trigger async tasks
    """

    cart_items = cart.items.select_related(
        "variant",
        "variant__product",
    )

    if not cart_items.exists():
        raise EmptyCartException(
            "Cart is empty.",
        )

    subtotal_amount = Decimal(
        "0.00",
    )

    order = Order.objects.create(
        user=user,
        email=user.email,
        status=OrderStatus.PENDING,
        shipping_address=shipping_address,
        billing_address=(billing_address or shipping_address),
        shipping_method=shipping_method,
        subtotal_amount=Decimal(
            "0.00",
        ),
        shipping_amount=Decimal(
            "0.00",
        ),
        tax_amount=Decimal(
            "0.00",
        ),
        total_amount=Decimal(
            "0.00",
        ),
    )

    for item in cart_items:
        variant = item.variant

        if item.quantity <= 0:
            raise InvalidQuantityException(
                f"Invalid quantity for {variant.sku}",
            )

        inventory = Inventory.objects.select_for_update().get(
            variant=variant,
        )

        if inventory.available_quantity < item.quantity:
            raise InsufficientStockException(
                f"Insufficient stock for {variant.sku}",
            )

        line_total = variant.price * item.quantity

        subtotal_amount += line_total

        OrderItem.objects.create(
            order=order,
            variant=variant,
            product_name=variant.product.name,
            sku=variant.sku,
            quantity=item.quantity,
            unit_price=variant.price,
            total_price=line_total,
        )

    order.subtotal_amount = subtotal_amount

    order.shipping_amount = calculate_shipping_for_order(
        order,
    )

    order.tax_amount = calculate_tax_for_order(
        order,
    )

    discount_amount = Decimal(
        "0.00",
    )

    if discount_code:
        discount = Discount.objects.get(
            code=discount_code,
            active=True,
        )

        validate_discount(
            discount,
            order.subtotal_amount,
        )

        discount_amount = calculate_discount_amount(
            discount,
            order.subtotal_amount,
        )

        order.discount = discount

        order.discount_amount = discount_amount

        discount.used_count += 1

        discount.save(
            update_fields=[
                "used_count",
            ],
        )

    order.total_amount = (
        order.subtotal_amount
        + order.shipping_amount
        + order.tax_amount
        - discount_amount
    )

    order.save(
        update_fields=[
            "subtotal_amount",
            "shipping_amount",
            "tax_amount",
            "discount",
            "discount_amount",
            "total_amount",
        ],
    )

    create_audit_log(
        user=user,
        action="order_created",
        entity_type="order",
        entity_id=order.id,
        metadata={
            "total": str(
                order.total_amount,
            ),
        },
    )

    dispatch_event(
        OrderCreatedEvent(
            payload={
                "order": order,
            },
        ),
    )

    reserve_inventory_for_order(
        order,
    )

    create_payment_for_order(
        order=order,
    )

    send_order_confirmation_email.delay(
        order.id,
    )

    cart.items.all().delete()

    logger.info((f"Order created {order.id} for user {user.id}"))

    return order
