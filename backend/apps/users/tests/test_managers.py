import pytest
from django.contrib.auth import (
    get_user_model,
)

User = get_user_model()


pytestmark = pytest.mark.django_db


def test_create_user():
    """
    Manager creates regular user.
    """

    user = User.objects.create_user(
        email="test@example.com",
        password="StrongPassword123!",
    )

    assert user.email == "test@example.com"

    assert user.check_password("StrongPassword123!")


def test_create_user_requires_email():
    """
    Email is mandatory.
    """

    with pytest.raises(
        ValueError,
        match="Email is required",
    ):
        User.objects.create_user(
            email="",
            password="StrongPassword123!",
        )


def test_create_user_normalizes_email():
    """
    Email should be normalized.
    """

    user = User.objects.create_user(
        email="TEST@EXAMPLE.COM",
        password="StrongPassword123!",
    )

    assert user.email == "TEST@example.com"


def test_create_superuser():
    """
    Manager creates superuser.
    """

    user = User.objects.create_superuser(
        email="admin@example.com",
        password="StrongPassword123!",
    )

    assert user.is_staff is True

    assert user.is_superuser is True

    assert user.is_active is True
