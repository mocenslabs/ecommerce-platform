import pytest

from apps.authentication.api.services.auth import (
    authenticate_user,
    generate_tokens_for_user,
)

pytestmark = pytest.mark.django_db


def test_authenticate_user_success(
    user,
):
    """
    Authenticate valid user.
    """

    authenticated_user = authenticate_user(
        email=user.email,
        password="StrongPassword123!",
    )

    assert authenticated_user == user


def test_authenticate_user_invalid_email():
    """
    Return None when user
    does not exist.
    """

    authenticated_user = authenticate_user(
        email="missing@example.com",
        password="StrongPassword123!",
    )

    assert authenticated_user is None


def test_authenticate_user_invalid_password(
    user,
):
    """
    Return None when password
    is invalid.
    """

    authenticated_user = authenticate_user(
        email=user.email,
        password="wrong-password",
    )

    assert authenticated_user is None


def test_generate_tokens_for_user(
    user,
):
    """
    Generate access and refresh tokens.
    """

    tokens = generate_tokens_for_user(
        user,
    )

    assert "access" in tokens

    assert "refresh" in tokens
