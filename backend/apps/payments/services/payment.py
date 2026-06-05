from apps.audit.services import (
    create_audit_log,
)
from apps.payments.constants import (
    PaymentProvider,
    PaymentStatus,
)
from apps.payments.models import (
    Payment,
)
from apps.payments.providers.mercadopago import (
    MercadoPagoProvider,
)

PROVIDERS = {
    PaymentProvider.MERCADOPAGO: (MercadoPagoProvider),
}


def create_payment_for_order(
    order,
    provider=PaymentProvider.MERCADOPAGO,
):
    """
    Create payment instance and initialize provider flow.
    """

    payment = Payment.objects.create(
        order=order,
        provider=provider,
        amount=order.total_amount,
        status=PaymentStatus.PENDING,
    )

    provider_class = PROVIDERS[provider]

    provider_instance = provider_class()

    provider_response = provider_instance.create_payment(
        payment,
    )

    payment.external_id = provider_response.get(
        "external_id",
        "",
    )

    payment.raw_response = provider_response

    payment.save(
        update_fields=[
            "external_id",
            "raw_response",
        ],
    )

    create_audit_log(
        user=order.user,
        action="payment_created",
        entity_type="payment",
        entity_id=payment.id,
        metadata={
            "order_id": str(
                order.id,
            ),
            "amount": str(
                payment.amount,
            ),
            "provider": (payment.provider),
            "status": (payment.status),
        },
    )

    return payment
