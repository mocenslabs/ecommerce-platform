import pytest

from apps.users.models import UserRole
from apps.users.tests.factories import (
    AdminUserFactory,
    StaffUserFactory,
    UserFactory,
)

pytestmark = pytest.mark.django_db


def test_user_default_role():
    """
    User should be customer by default.
    """

    user = UserFactory()

    assert user.role == UserRole.CUSTOMER


def test_user_is_customer_property():
    """
    Customer property should return True.
    """

    user = UserFactory()

    assert user.is_customer is True

    assert user.is_admin_user is False

    assert user.is_staff_user is False


def test_user_is_admin_property():
    """
    Admin property should return True.
    """

    user = AdminUserFactory()

    assert user.is_admin_user is True

    assert user.is_customer is False


def test_user_is_staff_property():
    """
    Staff property should return True.
    """

    user = StaffUserFactory()

    assert user.is_staff_user is True

    assert user.is_customer is False


def test_verify_email():
    """
    User email can be verified.
    """

    user = UserFactory(
        is_verified=False,
    )

    assert user.is_verified is False

    assert user.verified_at is None

    user.verify_email()

    user.refresh_from_db()

    assert user.is_verified is True

    assert user.verified_at is not None


def test_admin_role_sets_is_staff():
    """
    Admin role should enable is_staff.
    """

    user = AdminUserFactory()

    assert user.is_staff is True


def test_staff_role_sets_is_staff():
    """
    Staff role should enable is_staff.
    """

    user = StaffUserFactory()

    assert user.is_staff is True


def test_user_has_uuid():
    """
    User should have UUID primary key.
    """

    user = UserFactory()

    assert user.id is not None
