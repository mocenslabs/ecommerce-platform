import factory
from django.contrib.auth import get_user_model

from apps.users.models.roles import UserRole

User = get_user_model()


class UserFactory(
    factory.django.DjangoModelFactory,
):
    """
    User factory.
    """

    class Meta:
        model = User

        skip_postgeneration_save = True

    email = factory.Sequence(lambda n: f"user{n}@example.com")

    first_name = factory.Faker("first_name")

    last_name = factory.Faker("last_name")

    role = UserRole.CUSTOMER

    is_active = True

    is_verified = True

    @factory.post_generation
    def password(
        self,
        create,
        extracted,
        **kwargs,
    ):
        """
        Set hashed password.
        """

        password = extracted or "StrongPassword123!"

        self.set_password(
            password,
        )

        if create:
            self.save(
                update_fields=[
                    "password",
                ]
            )


class AdminUserFactory(
    UserFactory,
):
    """
    Admin user factory.
    """

    role = UserRole.ADMIN


class StaffUserFactory(
    UserFactory,
):
    """
    Staff user factory.
    """

    role = UserRole.STAFF


class UnverifiedUserFactory(
    UserFactory,
):
    """
    Unverified user factory.
    """

    is_verified = False
