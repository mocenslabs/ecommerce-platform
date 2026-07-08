from decimal import Decimal

from django.core.management.base import BaseCommand

from apps.catalog.models import (
    Brand,
    Category,
    Product,
    ProductVariant,
)
from apps.inventory.models import (
    Inventory,
)


class Command(BaseCommand):
    help = "Seed demo ecommerce store"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating demo store...")

        categories = {
            "Electronics": [
                ("iPhone 15 Pro", "Latest Apple smartphone"),
                ("Galaxy S25 Ultra", "Samsung flagship device"),
                ("MacBook Air M4", "Lightweight productivity laptop"),
                ("Sony WH-1000XM5", "Premium noise cancelling headphones"),
            ],
            "Gaming": [
                ("PlayStation 5", "Next generation gaming console"),
                ("Xbox Series X", "Powerful Microsoft console"),
                ("Nintendo Switch OLED", "Portable gaming console"),
                ("Gaming Headset Pro", "Immersive gaming audio"),
            ],
            "Fashion": [
                ("Nike Air Max", "Comfortable running shoes"),
                ("Adidas Ultraboost", "Premium sports footwear"),
                ("Classic Hoodie", "Everyday casual hoodie"),
                ("Slim Fit Jeans", "Modern denim style"),
            ],
            "Sports": [
                ("Football Pro", "Professional football"),
                ("Basketball Elite", "Indoor and outdoor basketball"),
                ("Training Gloves", "Workout support gloves"),
                ("Yoga Mat", "Comfort fitness mat"),
            ],
            "Home": [
                ("Smart Lamp", "WiFi enabled lamp"),
                ("Coffee Maker", "Automatic coffee machine"),
                ("Air Purifier", "Cleaner indoor air"),
                ("Robot Vacuum", "Automated cleaning device"),
            ],
        }

        brands = [
            "Apple",
            "Samsung",
            "Sony",
            "Nike",
            "Adidas",
        ]

        brand_objects = {}

        for brand_name in brands:
            brand, _ = Brand.objects.get_or_create(
                name=brand_name,
            )

            brand_objects[brand_name] = brand

        featured_count = 0

        for category_name, products in categories.items():
            category, _ = Category.objects.get_or_create(
                name=category_name,
            )

            for index, (
                product_name,
                description,
            ) in enumerate(products):
                brand = list(brand_objects.values())[index % len(brand_objects)]

                product, _ = Product.objects.get_or_create(
                    name=product_name,
                    defaults={
                        "short_description": description,
                        "description": description,
                        "category": category,
                        "brand": brand,
                        "is_featured": featured_count < 6,
                    },
                )

                if featured_count < 6:
                    featured_count += 1

                standard_variant, _ = ProductVariant.objects.get_or_create(
                    product=product,
                    sku=f"{product.slug}-standard",
                    defaults={
                        "price": Decimal("99.99") + Decimal(index * 100),
                        "attributes": {
                            "type": "Standard",
                        },
                    },
                )

                Inventory.objects.get_or_create(
                    variant=standard_variant,
                    defaults={
                        "quantity": 100,
                        "reserved_quantity": 0,
                    },
                )

                premium_variant, _ = ProductVariant.objects.get_or_create(
                    product=product,
                    sku=f"{product.slug}-premium",
                    defaults={
                        "price": Decimal("149.99") + Decimal(index * 100),
                        "attributes": {
                            "type": "Premium",
                        },
                    },
                )

                Inventory.objects.get_or_create(
                    variant=premium_variant,
                    defaults={
                        "quantity": 100,
                        "reserved_quantity": 0,
                    },
                )

        self.stdout.write(self.style.SUCCESS("Demo store created successfully."))
