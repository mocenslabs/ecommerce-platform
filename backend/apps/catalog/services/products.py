from apps.catalog.models import Product


def create_product(**data):
    return Product.objects.create(**data)
