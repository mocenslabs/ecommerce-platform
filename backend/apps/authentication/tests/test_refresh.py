import pytest
from rest_framework_simplejwt.tokens import (
    RefreshToken,
)

pytestmark = pytest.mark.django_db


def test_refresh_token_success(
    api_client,
    user,
):
    """
    User can refresh access token.
    """

    refresh = RefreshToken.for_user(
        user,
    )

    response = api_client.post(
        "/api/v1/auth/refresh/",
        {
            "refresh": str(refresh),
        },
        format="json",
    )

    assert response.status_code == 200

    data = response.json()

    assert "access" in data


def test_refresh_token_invalid(
    api_client,
):
    """
    Refresh fails with invalid token.
    """

    response = api_client.post(
        "/api/v1/auth/refresh/",
        {
            "refresh": "invalid-token",
        },
        format="json",
    )

    assert response.status_code == 401
