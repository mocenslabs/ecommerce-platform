import pytest

from apps.cart.models import Cart
from apps.catalog.models import (
    Category,
    Product,
    ProductVariant,
)
from apps.inventory.models import Inventory
from apps.orders.models import (
    Address,
    ShippingMethod,
)
from apps.orders.tests.factories.order_factory import (
    OrderFactory,
)
from apps.users.models import User


@pytest.fixture
def user():
    """
    Reusable user fixture.
    """

    return User.objects.create_user(
        email="test@example.com",
        password="testpass123",
    )


@pytest.fixture
def category():
    """
    Reusable category fixture.
    """

    return Category.objects.create(
        name="Test Category",
        slug="test-category",
    )


@pytest.fixture
def product(
    category,
):
    """
    Reusable product fixture.
    """

    return Product.objects.create(
        category=category,
        name="Test Product",
        slug="test-product",
        description="Test description",
        is_active=True,
    )


@pytest.fixture
def variant(
    product,
):
    """
    Reusable variant fixture.
    """

    variant = ProductVariant.objects.create(
        product=product,
        sku="TEST-SKU",
        price="100.00",
        compare_at_price="120.00",
        is_active=True,
    )

    Inventory.objects.create(
        variant=variant,
        quantity=10,
        reserved_quantity=0,
    )

    return variant


@pytest.fixture
def cart(
    user,
):
    """
    Empty cart fixture.
    """

    return Cart.objects.create(
        user=user,
    )


@pytest.fixture
def cart_with_items(
    cart,
    variant,
):
    """
    Cart with products fixture.
    """

    cart.items.create(
        variant=variant,
        quantity=1,
    )

    return cart


@pytest.fixture
def shipping_address(
    user,
):
    """
    Reusable shipping address fixture.
    """

    return Address.objects.create(
        user=user,
        first_name="John",
        last_name="Doe",
        line_1="Main Street 123",
        line_2="",
        city="New York",
        state="NY",
        postal_code="10001",
        country="US",
        phone_number="+123456789",
    )


@pytest.fixture
def shipping_method():
    """
    Reusable shipping method fixture.
    """

    return ShippingMethod.objects.create(
        name="Standard",
        code="standard",
        price="10.00",
        is_active=True,
    )


@pytest.fixture
def order():
    """
    Reusable order fixture.
    """

    return OrderFactory()
