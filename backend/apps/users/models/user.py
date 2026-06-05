import uuid

from django.contrib.auth.models import (
    AbstractUser,
)
from django.db import models
from django.utils import timezone

from apps.users.models.managers import (
    UserManager,
)
from apps.users.models.roles import (
    UserRole,
)


class User(AbstractUser):
    """
    Custom user model.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    username = None

    email = models.EmailField(
        unique=True,
    )

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CUSTOMER,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    verified_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_customer(
        self,
    ):
        """
        Return whether user is customer.
        """

        return self.role == UserRole.CUSTOMER

    @property
    def is_admin_user(
        self,
    ):
        """
        Return whether user is admin.
        """

        return self.role == UserRole.ADMIN

    @property
    def is_staff_user(
        self,
    ):
        """
        Return whether user is staff.
        """

        return self.role == UserRole.STAFF

    def verify_email(
        self,
    ):
        """
        Mark user email as verified.
        """

        self.is_verified = True

        self.verified_at = timezone.now()

        self.save(
            update_fields=[
                "is_verified",
                "verified_at",
            ],
        )

    def save(
        self,
        *args,
        **kwargs,
    ):
        """
        Sync Django staff flags
        with custom roles.
        """

        if self.role in [
            UserRole.ADMIN,
            UserRole.STAFF,
        ]:
            self.is_staff = True

        super().save(
            *args,
            **kwargs,
        )
