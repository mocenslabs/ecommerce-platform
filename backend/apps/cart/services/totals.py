from decimal import Decimal


def calculate_cart_subtotal(cart):
    subtotal = Decimal("0.00")

    for item in cart.items.all():
        subtotal += item.variant.price * item.quantity

    return subtotal
