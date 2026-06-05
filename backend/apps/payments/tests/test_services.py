import pytest

from apps.payments.constants import (
    PaymentProvider,
)
from apps.payments.services.payment import (
    create_payment_for_order,
)


@pytest.mark.django_db
def test_create_payment_for_order(order):
    payment = create_payment_for_order(
        order=order,
        provider=PaymentProvider.MERCADOPAGO,
    )

    assert payment.provider == (PaymentProvider.MERCADOPAGO)

    assert payment.external_id == "mp_test_123"
