class BaseTaxStrategy:
    """
    Base tax strategy.
    """

    def calculate(
        self,
        order,
    ):
        raise NotImplementedError
