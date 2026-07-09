# Authentication API Reference

## Overview

The Authentication application manages user authentication, authorization, token lifecycle, email verification, and password recovery.

It is responsible for the complete authentication workflow of the platform.

Authentication is implemented using JWT (JSON Web Tokens).

---

# Responsibilities

The module provides:

- User registration
- User login
- JWT refresh
- Logout
- Current user profile
- Email verification
- Password reset
- Administrative authentication testing

---

# Base URL

```text
/api/v1/auth/
```

---

# Available Endpoints

| Method | Endpoint | Authentication | Description |
|----------|--------------------------|----------------|-----------------------------|
| POST | /register/ | Public | Register a new account |
| POST | /login/ | Public | Authenticate user |
| GET | /me/ | JWT | Return authenticated user |
| POST | /refresh/ | Refresh Token | Generate new access token |
| POST | /logout/ | JWT | Logout current user |
| GET | /admin-test/ | Admin | Permission verification |
| POST | /verify-email/ | Public | Verify email token |
| POST | /password-reset/ | Public | Request password reset |
| POST | /password-reset-confirm/ | Public | Set new password |

---

# Authentication Flow

Registration

↓

Email Verification

↓

Login

↓

Access Token

↓

Authenticated Requests

↓

Refresh Token

↓

Logout

---

# JWT Strategy

Authentication uses:

- Access Token
- Refresh Token

Every protected endpoint requires:

Authorization: Bearer <access_token>

---

# Current User Endpoint

Endpoint

GET /api/v1/auth/me/

Purpose

Returns the authenticated user profile.

Typical use:

- Navbar
- Profile page
- Session restoration

---

# Email Verification

The module includes a dedicated email verification flow.

Purpose:

- Validate account ownership
- Prevent fake registrations

---

# Password Recovery

Password recovery is divided into two steps.

Step 1

Request reset token

↓

Step 2

Confirm new password

This separation follows security best practices.

---

# Internal Architecture

Current structure

authentication/

api/

├── serializers/

├── services/

├── views/

└── urls.py

Business logic is delegated to the service layer whenever possible.

---

# Related Documentation

- Users
- Permissions
- Error Handling
- Security
