from rest_framework.throttling import (
    ScopedRateThrottle,
)


class LoginRateThrottle(
    ScopedRateThrottle,
):
    """
    Login protection throttle.
    """

    scope = "login"


class CheckoutRateThrottle(
    ScopedRateThrottle,
):
    """
    Checkout protection throttle.
    """

    scope = "checkout"


class WebhookRateThrottle(
    ScopedRateThrottle,
):
    """
    Payment webhook throttle.
    """

    scope = "webhook"
