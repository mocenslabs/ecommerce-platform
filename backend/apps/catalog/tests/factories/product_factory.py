import factory

from apps.catalog.models import Product

from .brand_factory import BrandFactory
from .category_factory import CategoryFactory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Product {n}")

    category = factory.SubFactory(
        CategoryFactory,
    )

    brand = factory.SubFactory(
        BrandFactory,
    )
