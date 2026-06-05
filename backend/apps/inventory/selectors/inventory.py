from apps.inventory.models import Inventory


def get_inventory_for_variant(variant_id):
    """
    Retrieve inventory information for a product variant.

    Args:
        variant_id: ProductVariant primary key.

    Returns:
        Inventory: Inventory instance.
    """
    return Inventory.objects.select_related(
        "variant",
    ).get(
        variant_id=variant_id,
    )
