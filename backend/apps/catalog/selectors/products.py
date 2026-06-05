from apps.catalog.models import Product


def get_active_products():
    return (
        Product.objects.filter(
            is_active=True,
        )
        .select_related(
            "category",
            "brand",
        )
        .prefetch_related(
            "variants",
            "images",
        )
    )
