from django.contrib.auth.tokens import (
    default_token_generator,
)
from django.utils.encoding import (
    force_bytes,
    force_str,
)
from django.utils.http import (
    urlsafe_base64_decode,
    urlsafe_base64_encode,
)

from apps.users.models import (
    User,
)


def generate_email_verification_token(
    user,
):
    """
    Generate email verification token.
    """

    uid = urlsafe_base64_encode(force_bytes(user.pk))

    token = default_token_generator.make_token(
        user,
    )

    return {
        "uid": uid,
        "token": token,
    }


def verify_email_token(
    *,
    uid,
    token,
):
    """
    Validate email verification token.
    """

    try:
        user_id = force_str(urlsafe_base64_decode(uid))

        user = User.objects.get(
            pk=user_id,
        )

    except (
        TypeError,
        ValueError,
        OverflowError,
        User.DoesNotExist,
    ):
        return None

    is_valid = default_token_generator.check_token(
        user,
        token,
    )

    if not is_valid:
        return None

    return user
