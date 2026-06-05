from django.urls import path

from apps.authentication.api.views.admin_test import (
    AdminTestView,
)
from apps.authentication.api.views.login import (
    LoginView,
)
from apps.authentication.api.views.logout import (
    LogoutView,
)
from apps.authentication.api.views.me import (
    MeView,
)
from apps.authentication.api.views.password_reset import (
    PasswordResetConfirmView,
    PasswordResetRequestView,
)
from apps.authentication.api.views.refresh import (
    RefreshTokenView,
)
from apps.authentication.api.views.register import (
    RegisterView,
)
from apps.authentication.api.views.verification import (
    VerifyEmailApi,
)

urlpatterns = [
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "me/",
        MeView.as_view(),
        name="me",
    ),
    path(
        "refresh/",
        RefreshTokenView.as_view(),
        name="token_refresh",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "admin-test/",
        AdminTestView.as_view(),
        name="admin_test",
    ),
    path(
        "verify-email/",
        VerifyEmailApi.as_view(),
        name="verify-email",
    ),
    path(
        "password-reset/",
        PasswordResetRequestView.as_view(),
        name="password-reset",
    ),
    path(
        "password-reset-confirm/",
        PasswordResetConfirmView.as_view(),
        name="password-reset-confirm",
    ),
]
