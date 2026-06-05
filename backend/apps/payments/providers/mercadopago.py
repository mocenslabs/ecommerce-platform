from apps.payments.services.transactions import (
    create_payment_transaction,
)


class MercadoPagoProvider:
    """
    MercadoPago payment provider.
    """

    def create_payment(
        self,
        payment,
    ):
        """
        Create MercadoPago payment.
        """

        request_payload = {
            "payment_id": str(
                payment.payment_id,
            ),
            "amount": str(
                payment.amount,
            ),
        }

        response_payload = {
            "provider": "mercadopago",
            "status": "approved",
            "external_id": "mp_test_123",
            "checkout_url": ("https://mercadopago.com/checkout/test"),
        }

        create_payment_transaction(
            payment=payment,
            provider="mercadopago",
            transaction_type="create_payment",
            status="approved",
            success=True,
            request_payload=request_payload,
            response_payload=response_payload,
            raw_payload=response_payload,
            external_transaction_id="mp_mock_001",
        )

        return response_payload
