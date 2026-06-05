from unittest.mock import patch

import pytest
from django.contrib.auth import (
    get_user_model,
)

User = get_user_model()


pytestmark = pytest.mark.django_db


@patch("apps.authentication.api.views.register.create_audit_log")
@patch("apps.authentication.api.views.register.send_verification_email.delay")
def test_register_user_success(
    mock_task,
    mock_audit,
    api_client,
):
    """
    User can register successfully.
    """

    payload = {
        "email": "newuser@example.com",
        "password": "StrongPassword123!",
        "first_name": "John",
        "last_name": "Doe",
    }

    response = api_client.post(
        "/api/v1/auth/register/",
        payload,
        format="json",
    )

    assert response.status_code == 201

    assert User.objects.filter(email="newuser@example.com").exists()

    data = response.json()

    assert "tokens" in data

    assert "access" in data["tokens"]

    assert "refresh" in data["tokens"]

    mock_task.assert_called_once()

    mock_audit.assert_called_once()


def test_register_duplicate_email(
    api_client,
    user,
):
    """
    Registration fails when email already exists.
    """

    payload = {
        "email": user.email,
        "password": "StrongPassword123!",
    }

    response = api_client.post(
        "/api/v1/auth/register/",
        payload,
        format="json",
    )

    assert response.status_code == 400

    assert "email" in response.json()["errors"]


def test_register_weak_password(
    api_client,
):
    """
    Registration fails with weak password.
    """

    payload = {
        "email": "weak@example.com",
        "password": "12345678",
    }

    response = api_client.post(
        "/api/v1/auth/register/",
        payload,
        format="json",
    )

    assert response.status_code == 400
