import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"user{n}@example.com")

    first_name = "John"

    last_name = "Doe"

    is_verified = True

    is_active = True

    password = factory.PostGenerationMethodCall(
        "set_password",
        "StrongPass123!",
    )
