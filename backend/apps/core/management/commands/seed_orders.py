from django.contrib.auth import (
    get_user_model,
)
from django.core.management.base import (
    BaseCommand,
)

from apps.orders.models import (
    Address,
    ShippingMethod,
)

User = get_user_model()


class Command(BaseCommand):
    help = "Seed orders data."

    def handle(
        self,
        *args,
        **kwargs,
    ):
        self.create_shipping_methods()

        self.create_default_address()

        self.stdout.write(self.style.SUCCESS("Orders seed completed."))

    def create_shipping_methods(
        self,
    ):
        methods = [
            {
                "name": "Standard Shipping",
                "code": "standard",
                "price": 9.99,
                "estimated_days": 5,
            },
            {
                "name": "Express Shipping",
                "code": "express",
                "price": 19.99,
                "estimated_days": 2,
            },
            {
                "name": "Premium Shipping",
                "code": "premium",
                "price": 29.99,
                "estimated_days": 1,
            },
        ]

        for method in methods:
            ShippingMethod.objects.get_or_create(
                code=method["code"],
                defaults=method,
            )

    def create_default_address(
        self,
    ):
        user = User.objects.first()

        if not user:
            return

        Address.objects.get_or_create(
            user=user,
            is_default=True,
            defaults={
                "first_name": "Mauro",
                "last_name": "Vicens",
                "line_1": "Demo Street 123",
                "line_2": "",
                "city": "Armstrong",
                "state": "Santa Fe",
                "postal_code": "2508",
                "country": "AR",
                "phone_number": "+543471000000",
                "is_billing": True,
                "is_shipping": True,
            },
        )
