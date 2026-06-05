from unittest.mock import patch

import pytest

from apps.authentication.api.services.verification import (
    generate_email_verification_token,
)

pytestmark = pytest.mark.django_db


@patch("apps.authentication.api.views.verification.create_audit_log")
def test_verify_email_success(
    mock_audit,
    api_client,
    unverified_user,
):
    """
    User can verify email successfully.
    """

    tokens = generate_email_verification_token(
        unverified_user,
    )

    response = api_client.post(
        "/api/v1/auth/verify-email/",
        {
            "uid": tokens["uid"],
            "token": tokens["token"],
        },
        format="json",
    )

    assert response.status_code == 200

    unverified_user.refresh_from_db()

    assert unverified_user.is_verified is True

    assert unverified_user.verified_at is not None

    mock_audit.assert_called_once()


def test_verify_email_invalid_token(
    api_client,
    unverified_user,
):
    """
    Verification fails with invalid token.
    """

    tokens = generate_email_verification_token(
        unverified_user,
    )

    response = api_client.post(
        "/api/v1/auth/verify-email/",
        {
            "uid": tokens["uid"],
            "token": "invalid-token",
        },
        format="json",
    )

    assert response.status_code == 400

    unverified_user.refresh_from_db()

    assert unverified_user.is_verified is False
