from django.contrib import admin

from .models import (
    Address,
    Order,
    OrderItem,
)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = (
        "product_name",
        "sku",
        "quantity",
        "unit_price",
        "total_price",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "email",
        "status",
        "total_amount",
        "created_at",
    )

    list_filter = ("status",)

    search_fields = (
        "order_number",
        "email",
    )

    readonly_fields = (
        "subtotal_amount",
        "total_amount",
    )

    inlines = [OrderItemInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "city",
        "country",
    )
