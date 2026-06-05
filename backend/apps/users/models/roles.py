from django.db import models


class UserRole(models.TextChoices):
    """
    Available user roles.
    """

    CUSTOMER = (
        "customer",
        "Customer",
    )

    ADMIN = (
        "admin",
        "Admin",
    )

    STAFF = (
        "staff",
        "Staff",
    )
