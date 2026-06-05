from django.contrib import admin

from .models import (
    Payment,
    Transaction,
)


class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0
    readonly_fields = (
        "transaction_id",
        "transaction_type",
        "status",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "payment_id",
        "provider",
        "status",
        "amount",
        "created_at",
    )

    list_filter = (
        "provider",
        "status",
    )

    readonly_fields = (
        "idempotency_key",
        "raw_response",
    )

    inlines = [TransactionInline]
