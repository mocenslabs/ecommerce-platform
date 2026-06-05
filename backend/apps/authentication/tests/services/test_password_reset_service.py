import pytest

from apps.authentication.api.services.password_reset import (
    generate_password_reset_token,
    validate_password_reset_token,
)

pytestmark = pytest.mark.django_db


def test_generate_password_reset_token(
    user,
):
    """
    Generate reset token.
    """

    data = generate_password_reset_token(
        user,
    )

    assert "uid" in data

    assert "token" in data


def test_validate_password_reset_token_success(
    user,
):
    """
    Validate generated token.
    """

    data = generate_password_reset_token(
        user,
    )

    validated_user = validate_password_reset_token(
        uid=data["uid"],
        token=data["token"],
    )

    assert validated_user == user


def test_validate_password_reset_token_invalid_uid():
    """
    Invalid uid returns None.
    """

    user = validate_password_reset_token(
        uid="invalid",
        token="invalid",
    )

    assert user is None
