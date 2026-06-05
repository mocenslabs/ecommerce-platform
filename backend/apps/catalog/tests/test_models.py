import pytest

from apps.catalog.tests.factories.product_factory import (
    ProductFactory,
)


@pytest.mark.django_db
def test_product_creation():
    product = ProductFactory()

    assert product.id is not None
    assert product.name is not None
