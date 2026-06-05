from django.contrib import admin

from apps.discounts.models import (
    Discount,
)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "discount_type",
        "value",
        "active",
        "used_count",
        "expires_at",
    ]

    search_fields = [
        "code",
    ]

    list_filter = [
        "discount_type",
        "active",
    ]
