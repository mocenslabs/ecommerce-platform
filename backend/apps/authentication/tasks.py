from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from apps.authentication.api.services.password_reset import (
    generate_password_reset_token,
)
from apps.authentication.api.services.verification import (
    generate_email_verification_token,
)
from apps.core.tasks import (
    BaseTaskWithRetry,
)
from apps.users.models import (
    User,
)


@shared_task(
    bind=True,
    base=BaseTaskWithRetry,
)
def send_verification_email(
    self,
    user_id,
):
    """
    Send verification email asynchronously.
    """

    user = User.objects.get(
        pk=user_id,
    )

    tokens = generate_email_verification_token(
        user,
    )

    verification_url = (
        "http://localhost:5173/verify-email/"
        f"?uid={tokens['uid']}"
        f"&token={tokens['token']}"
    )

    send_mail(
        subject=("Verify your account"),
        message=(f"Verify your account:\n\n{verification_url}"),
        from_email=(settings.DEFAULT_FROM_EMAIL),
        recipient_list=[
            user.email,
        ],
        fail_silently=False,
    )


@shared_task(
    bind=True,
    base=BaseTaskWithRetry,
)
def send_password_reset_email(
    self,
    user_id,
):
    """
    Send password reset email.
    """

    user = User.objects.get(
        pk=user_id,
    )

    tokens = generate_password_reset_token(
        user,
    )

    reset_url = (
        "http://localhost:5173/reset-password/"
        f"?uid={tokens['uid']}"
        f"&token={tokens['token']}"
    )

    send_mail(
        subject=("Reset your password"),
        message=(f"Reset your password:\n\n{reset_url}"),
        from_email=(settings.DEFAULT_FROM_EMAIL),
        recipient_list=[
            user.email,
        ],
        fail_silently=False,
    )
