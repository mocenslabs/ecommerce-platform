class BaseShippingStrategy:
    """
    Base shipping strategy.
    """

    def calculate(
        self,
        order,
    ):
        raise NotImplementedError
