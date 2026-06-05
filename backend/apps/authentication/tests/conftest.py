import pytest
from rest_framework.test import (
    APIClient,
)

from apps.users.tests.factories import (
    AdminUserFactory,
    UnverifiedUserFactory,
    UserFactory,
)


@pytest.fixture
def api_client():
    """
    Return API client.
    """

    return APIClient()


@pytest.fixture
def user():
    """
    Return regular user.
    """

    return UserFactory()


@pytest.fixture
def admin_user():
    """
    Return admin user.
    """

    return AdminUserFactory()


@pytest.fixture
def unverified_user():
    """
    Return unverified user.
    """

    return UnverifiedUserFactory()
