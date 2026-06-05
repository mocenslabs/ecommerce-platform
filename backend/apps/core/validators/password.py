import re

from django.core.exceptions import (
    ValidationError,
)


class StrongPasswordValidator:
    """
    Validate password strength.
    """

    def validate(
        self,
        password,
        user=None,
    ):
        """
        Validate strong password rules.
        """

        if not re.search(
            r"[A-Z]",
            password,
        ):
            raise ValidationError(
                ("Password must contain at least one uppercase letter.")
            )

        if not re.search(
            r"[a-z]",
            password,
        ):
            raise ValidationError(
                ("Password must contain at least one lowercase letter.")
            )

        if not re.search(
            r"\d",
            password,
        ):
            raise ValidationError(("Password must contain at least one number."))

        if not re.search(
            r"[!@#$%^&*(),.?\":{}|<>]",
            password,
        ):
            raise ValidationError(
                ("Password must contain at least one special character.")
            )

    def get_help_text(
        self,
    ):
        """
        Return validator help text.
        """

        return (
            "Password must contain uppercase, lowercase, number and special character."
        )
