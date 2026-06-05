class EmptyCartException(
    Exception,
):
    """
    Raised when checkout is attempted
    with an empty cart.
    """

    pass


class InsufficientStockException(Exception):
    """
    Raised when product stock
    is insufficient.
    """


class InvalidQuantityException(Exception):
    """
    Raised when quantity is invalid.
    """
