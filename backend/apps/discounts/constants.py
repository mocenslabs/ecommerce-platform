class DiscountType:
    """
    Available discount types.
    """

    PERCENTAGE = "percentage"

    FIXED = "fixed"

    CHOICES = [
        (
            PERCENTAGE,
            "Percentage",
        ),
        (
            FIXED,
            "Fixed",
        ),
    ]
