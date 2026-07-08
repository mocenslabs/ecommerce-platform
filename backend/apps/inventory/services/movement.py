from apps.inventory.constants import (
    InventoryMovementType,
)
from apps.inventory.models import (
    InventoryMovement,
)


def create_inventory_movement(
    *,
    variant,
    movement_type,
    quantity_change,
    reference_type="",
    reference_id="",
    created_by=None,
    notes="",
):
    """
    Create inventory movement record.

    Every inventory modification should generate
    a movement entry for auditability.

    Args:
        variant:
            ProductVariant instance.

        movement_type:
            Inventory movement type.

        quantity_change:
            Positive or negative quantity.

        reference_type:
            Source entity type.

        reference_id:
            Source entity identifier.

        created_by:
            Optional user.

        notes:
            Optional notes.

    Returns:
        InventoryMovement
    """

    return InventoryMovement.objects.create(
        variant=variant,
        movement_type=movement_type,
        quantity_change=quantity_change,
        reference_type=reference_type,
        reference_id=str(reference_id),
        created_by=created_by,
        notes=notes,
    )
