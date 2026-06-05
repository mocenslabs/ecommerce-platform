import pytest
from rest_framework_simplejwt.tokens import (
    RefreshToken,
)

pytestmark = pytest.mark.django_db


def test_admin_endpoint_success(
    api_client,
    admin_user,
):
    """
    Admin can access endpoint.
    """

    refresh = RefreshToken.for_user(
        admin_user,
    )

    api_client.credentials(HTTP_AUTHORIZATION=(f"Bearer {refresh.access_token}"))

    response = api_client.get(
        "/api/v1/auth/admin-test/",
    )

    assert response.status_code == 200


def test_admin_endpoint_forbidden(
    api_client,
    user,
):
    """
    Customer cannot access endpoint.
    """

    refresh = RefreshToken.for_user(
        user,
    )

    api_client.credentials(HTTP_AUTHORIZATION=(f"Bearer {refresh.access_token}"))

    response = api_client.get(
        "/api/v1/auth/admin-test/",
    )

    assert response.status_code == 403
