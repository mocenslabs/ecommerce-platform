from rest_framework.permissions import (
    BasePermission,
)

from apps.users.models import (
    UserRole,
)


class IsAdminUserRole(
    BasePermission,
):
    """
    Allow access only to admin users.
    """

    def has_permission(
        self,
        request,
        view,
    ):
        """
        Validate admin role access.
        """

        return request.user.is_authenticated and request.user.role == UserRole.ADMIN


class IsStaffUserRole(
    BasePermission,
):
    """
    Allow access only to staff users.
    """

    def has_permission(
        self,
        request,
        view,
    ):
        """
        Validate staff role access.
        """

        return request.user.is_authenticated and request.user.role in [
            UserRole.ADMIN,
            UserRole.STAFF,
        ]


class IsCustomerUserRole(
    BasePermission,
):
    """
    Allow access only to customer users.
    """

    def has_permission(
        self,
        request,
        view,
    ):
        """
        Validate customer role access.
        """

        return request.user.is_authenticated and request.user.role == UserRole.CUSTOMER
