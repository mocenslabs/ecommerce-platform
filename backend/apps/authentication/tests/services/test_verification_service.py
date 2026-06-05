import pytest

from apps.authentication.api.services.verification import (
    generate_email_verification_token,
    verify_email_token,
)

pytestmark = pytest.mark.django_db


def test_generate_email_verification_token(
    user,
):
    """
    Generate email verification token.
    """

    data = generate_email_verification_token(
        user,
    )

    assert "uid" in data

    assert "token" in data


def test_verify_email_token_success(
    user,
):
    """
    Verify generated token.
    """

    data = generate_email_verification_token(
        user,
    )

    validated_user = verify_email_token(
        uid=data["uid"],
        token=data["token"],
    )

    assert validated_user == user


def test_verify_email_token_invalid_uid():
    """
    Invalid uid returns None.
    """

    user = verify_email_token(
        uid="invalid",
        token="invalid",
    )

    assert user is None
