from unittest.mock import patch

import pytest

pytestmark = pytest.mark.django_db


@patch("apps.authentication.api.views.login.create_audit_log")
def test_login_success(
    mock_audit,
    api_client,
    user,
):
    """
    User can login successfully.
    """

    payload = {
        "email": user.email,
        "password": "StrongPassword123!",
    }

    response = api_client.post(
        "/api/v1/auth/login/",
        payload,
        format="json",
    )

    assert response.status_code == 200

    data = response.json()

    assert "tokens" in data

    assert "access" in data["tokens"]

    assert "refresh" in data["tokens"]

    mock_audit.assert_called_once()


def test_login_invalid_password(
    api_client,
    user,
):
    """
    Login fails with invalid password.
    """

    payload = {
        "email": user.email,
        "password": "WrongPassword123!",
    }

    response = api_client.post(
        "/api/v1/auth/login/",
        payload,
        format="json",
    )

    assert response.status_code == 400


def test_login_unverified_user(
    api_client,
    unverified_user,
):
    """
    Login fails for unverified user.
    """

    payload = {
        "email": unverified_user.email,
        "password": "StrongPassword123!",
    }

    response = api_client.post(
        "/api/v1/auth/login/",
        payload,
        format="json",
    )

    assert response.status_code == 400
