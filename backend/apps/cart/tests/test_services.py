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


@pytest.mark.django_db
def test_add_item_to_cart():
    cart = CartFactory()

    product = ProductFactory()

    variant = ProductVariant.objects.create(
        product=product,
        sku="SKU-1",
        price=100,
    )

    cart_item = add_item_to_cart(
        cart=cart,
        variant=variant,
        quantity=2,
    )

    assert cart_item.quantity == 2
