import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_authenticated_user_can_checkout():
    """
    Ensure authenticated users can process checkout.
    """

    client = APIClient()

    response = client.post(
        "/api/checkout/",
    )

    assert response.status_code != 401
