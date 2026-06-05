from unittest.mock import patch

import pytest
from rest_framework_simplejwt.tokens import (
    RefreshToken,
)

pytestmark = pytest.mark.django_db


@patch("apps.authentication.api.views.logout.create_audit_log")
def test_logout_success(
    mock_audit,
    api_client,
    user,
):
    """
    Authenticated user can logout.
    """

    refresh = RefreshToken.for_user(
        user,
    )

    api_client.credentials(HTTP_AUTHORIZATION=(f"Bearer {refresh.access_token}"))

    response = api_client.post(
        "/api/v1/auth/logout/",
        {
            "refresh": str(refresh),
        },
        format="json",
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True

    mock_audit.assert_called_once()


def test_logout_requires_authentication(
    api_client,
    user,
):
    """
    Anonymous users cannot logout.
    """

    refresh = RefreshToken.for_user(
        user,
    )

    response = api_client.post(
        "/api/v1/auth/logout/",
        {
            "refresh": str(refresh),
        },
        format="json",
    )

    assert response.status_code == 401


def test_logout_invalid_refresh_token(
    api_client,
    user,
):
    """
    Logout fails with invalid token.
    """

    refresh = RefreshToken.for_user(
        user,
    )

    api_client.credentials(HTTP_AUTHORIZATION=(f"Bearer {refresh.access_token}"))

    response = api_client.post(
        "/api/v1/auth/logout/",
        {
            "refresh": "invalid-token",
        },
        format="json",
    )

    assert response.status_code == 400
