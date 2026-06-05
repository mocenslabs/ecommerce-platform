import pytest

from apps.catalog.models import ProductVariant
from apps.catalog.tests.factories.product_factory import (
    ProductFactory,
)
from apps.inventory.models import Inventory
from apps.inventory.services.reservation import (
    reserve_inventory_for_order,
)
from apps.orders.models import OrderItem
from apps.orders.tests.factories.order_factory import OrderFactory


@pytest.mark.django_db
def test_reserve_inventory_for_order():
    product = ProductFactory()

    variant = ProductVariant.objects.create(
        product=product,
        sku="INV-1",
        price=100,
    )

    inventory = Inventory.objects.create(
        variant=variant,
        quantity=10,
    )

    order = OrderFactory()

    OrderItem.objects.create(
        order=order,
        product_name="Test",
        sku="INV-1",
        quantity=2,
        unit_price=100,
        total_price=200,
        variant=variant,
    )

    reserve_inventory_for_order(order)

    inventory.refresh_from_db()

    assert inventory.reserved_quantity == 2
