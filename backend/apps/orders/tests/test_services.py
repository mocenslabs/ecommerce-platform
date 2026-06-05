import pytest

from apps.cart.services.cart import (
    add_item_to_cart,
)
from apps.cart.tests.factories.cart_factory import (
    CartFactory,
)
from apps.catalog.models import ProductVariant
from apps.catalog.tests.factories.product_factory import (
    ProductFactory,
)
from apps.orders.models import Address
from apps.orders.services.order import (
    create_order_from_cart,
)


@pytest.mark.django_db
def test_create_order_from_cart():
    cart = CartFactory()

    product = ProductFactory()

    variant = ProductVariant.objects.create(
        product=product,
        sku="SKU-ORDER",
        price=100,
    )

    add_item_to_cart(
        cart=cart,
        variant=variant,
        quantity=2,
    )

    address = Address.objects.create(
        first_name="John",
        last_name="Doe",
        line_1="Street 123",
        city="City",
        state="State",
        postal_code="1234",
        country="AR",
        phone_number="123456",
    )

    order = create_order_from_cart(
        cart=cart,
        billing_address=address,
        shipping_address=address,
        email="test@test.com",
    )

    assert order.items.count() == 1
    assert order.total_amount == 200
