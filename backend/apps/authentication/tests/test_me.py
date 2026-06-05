import pytest
from rest_framework_simplejwt.tokens import (
    RefreshToken,
)

pytestmark = pytest.mark.django_db


def test_me_authenticated_user(
    api_client,
    user,
):
    """
    Authenticated user can retrieve profile.
    """

    refresh = RefreshToken.for_user(
        user,
    )

    api_client.credentials(HTTP_AUTHORIZATION=(f"Bearer {refresh.access_token}"))

    response = api_client.get(
        "/api/v1/auth/me/",
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == user.email


def test_me_requires_authentication(
    api_client,
):
    """
    Anonymous users cannot access profile.
    """

    response = api_client.get(
        "/api/v1/auth/me/",
    )

    assert response.status_code == 401
