from unittest.mock import patch

import pytest

from apps.authentication.api.services.password_reset import (
    generate_password_reset_token,
)

pytestmark = pytest.mark.django_db


@patch(
    "apps.authentication.api.serializers.password_reset.send_password_reset_email.delay"
)
@patch("apps.authentication.api.views.password_reset.create_audit_log")
def test_password_reset_request_success(
    mock_audit,
    mock_task,
    api_client,
    user,
):
    """
    User can request password reset.
    """

    response = api_client.post(
        "/api/v1/auth/password-reset/",
        {
            "email": user.email,
        },
        format="json",
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True

    mock_task.assert_called_once()

    mock_audit.assert_called_once()


def test_password_reset_request_unknown_email(
    api_client,
):
    """
    Password reset fails for unknown email.
    """

    response = api_client.post(
        "/api/v1/auth/password-reset/",
        {
            "email": "unknown@example.com",
        },
        format="json",
    )

    assert response.status_code == 400


@patch("apps.authentication.api.views.password_reset.create_audit_log")
def test_password_reset_confirm_success(
    mock_audit,
    api_client,
    user,
):
    """
    User can reset password successfully.
    """

    token_data = generate_password_reset_token(
        user,
    )

    response = api_client.post(
        "/api/v1/auth/password-reset-confirm/",
        {
            "uid": token_data["uid"],
            "token": token_data["token"],
            "password": "NewStrongPassword123!",
        },
        format="json",
    )

    assert response.status_code == 200

    user.refresh_from_db()

    assert user.check_password("NewStrongPassword123!")

    mock_audit.assert_called_once()


def test_password_reset_confirm_invalid_token(
    api_client,
    user,
):
    """
    Password reset fails with invalid token.
    """

    token_data = generate_password_reset_token(
        user,
    )

    response = api_client.post(
        "/api/v1/auth/password-reset-confirm/",
        {
            "uid": token_data["uid"],
            "token": "invalid-token",
            "password": "NewStrongPassword123!",
        },
        format="json",
    )

    assert response.status_code == 400
