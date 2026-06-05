from apps.payments.models import (
    Transaction,
)


def create_payment_transaction(
    payment,
    provider,
    transaction_type,
    status="success",
    success=False,
    request_payload=None,
    response_payload=None,
    raw_payload=None,
    error_message="",
    external_transaction_id="",
):
    """
    Create payment transaction log.
    """

    return Transaction.objects.create(
        payment=payment,
        provider=provider,
        transaction_id=(external_transaction_id),
        transaction_type=transaction_type,
        status=status,
        success=success,
        request_payload=request_payload or {},
        response_payload=response_payload or {},
        raw_payload=raw_payload or {},
        error_message=error_message,
    )
