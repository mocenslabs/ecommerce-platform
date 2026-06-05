from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.views import (
    TokenViewBase,
)


class RefreshTokenView(
    TokenViewBase,
):
    """
    Refresh JWT access token.
    """

    serializer_class = TokenRefreshSerializer
