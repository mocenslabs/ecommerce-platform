from django.contrib.auth import (
    get_user_model,
)
from rest_framework_simplejwt.tokens import (
    RefreshToken,
)

User = get_user_model()


def register_user(
    *,
    email,
    password,
    first_name="",
    last_name="",
):
    """
    Register new user.
    """

    user = User.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )

    return user


def authenticate_user(
    *,
    email,
    password,
):
    """
    Authenticate user credentials.
    """

    try:
        user = User.objects.get(
            email=email,
        )

    except User.DoesNotExist:
        return None

    if not user.check_password(
        password,
    ):
        return None

    return user


def generate_tokens_for_user(
    user,
):
    """
    Generate JWT tokens for user.
    """

    refresh = RefreshToken.for_user(
        user,
    )

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
