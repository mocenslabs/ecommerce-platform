import factory

from apps.orders.constants import OrderStatus
from apps.orders.models import (
    Address,
    Order,
)


class AddressFactory(factory.django.DjangoModelFactory):
    """
    Factory for reusable order addresses.
    """

    class Meta:
        model = Address

    first_name = "John"
    last_name = "Doe"
    line_1 = "Street 123"
    city = "Rosario"
    state = "Santa Fe"
    postal_code = "2508"
    country = "AR"
    phone_number = "123456789"


class OrderFactory(factory.django.DjangoModelFactory):
    """
    Factory for order testing scenarios.
    """

    class Meta:
        model = Order

    email = "test@test.com"

    status = OrderStatus.PENDING

    billing_address = factory.SubFactory(
        AddressFactory,
    )

    shipping_address = factory.SubFactory(
        AddressFactory,
    )

    subtotal_amount = 100
    total_amount = 100
