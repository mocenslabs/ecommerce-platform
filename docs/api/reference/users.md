# Users API Reference

## Overview

The Users application manages user profiles, account information, preferences and user-related resources.

Authentication is handled by the Authentication application, while this module is responsible for managing user data after successful authentication.

---

# Responsibilities

The Users application provides:

- User profile management
- Profile updates
- User information retrieval
- User preferences
- Administrative user management

---

# Base URL

```text
/api/v1/users/
```

---

# Main Resources

Primary resource

```text
User
```

Additional resources may include:

- User Profile
- Preferences
- Public Profile

---

# Available Endpoints

| Method | Endpoint | Authentication | Description |
|----------|----------------|----------------|---------------------------|
| GET | /me/ | JWT | Current user information |
| PATCH | /me/ | JWT | Update profile |
| GET | /<uuid>/ | Staff/Admin | Retrieve user |
| GET | / | Staff/Admin | User list |

---

# Current User

Endpoint

```http
GET /api/v1/users/me/
```

Purpose

Returns the authenticated user's information.

Typical frontend usage:

- Header
- Navigation
- Account page
- Checkout
- Dashboard

---

# Profile Update

Endpoint

```http
PATCH /api/v1/users/me/
```

Allows updating editable profile fields.

Typical editable fields include:

- First name
- Last name
- Avatar
- Phone
- Preferred language

Sensitive fields are handled by dedicated endpoints.

---

# Permissions

Regular users

May:

- View own profile
- Update own profile

Cannot:

- Access other users

---

Staff

May:

- View users
- Manage users according to assigned permissions

---

Administrators

Full access.

---

# Relationships

Users interact with:

- Orders
- Reviews
- Wishlist
- Cart
- Notifications
- Payments

---

# Frontend Integration

This module is commonly loaded immediately after authentication.

The frontend should cache the authenticated profile during the current session.

---

# Related Documentation

- Authentication
- Orders
- Reviews
- Wishlist
