# Authentication API

## Introduction

The authentication API provides secure access to user accounts and protected resources.

The system uses:

- JWT authentication.
- Access tokens.
- Refresh tokens.
- Role-based permissions.

---

# Authentication Flow

General flow:

```text
User

 |

Send Credentials

 |

Authentication Endpoint

 |

Validate Identity

 |

Generate JWT Tokens

 |

Return Tokens

 |

Authenticated Requests
```

---

# Authentication Endpoints

Base path:

```text
/api/v1/auth/
```

---

# Register User

## Endpoint

```http
POST /api/v1/auth/register/
```

## Description

Creates a new user account.

---

## Request Body

Example:

```json
{
    "email": "user@example.com",
    "password": "secure_password",
    "password_confirmation": "secure_password",
    "first_name": "John",
    "last_name": "Doe"
}
```

---

## Successful Response

Status:

```text
201 Created
```

Example:

```json
{
    "success": true,
    "message": "User created successfully",
    "data": {
        "id": 1,
        "email": "user@example.com"
    }
}
```

---

## Possible Errors

### Validation Error

Status:

```text
400 Bad Request
```

Example:

```json
{
    "success": false,
    "error": {
        "code": "validation_error",
        "message": "Invalid registration data"
    }
}
```

---

# Login

## Endpoint

```http
POST /api/v1/auth/login/
```

## Description

Authenticates a user and returns JWT tokens.

---

## Request Body

Example:

```json
{
    "email": "user@example.com",
    "password": "secure_password"
}
```

---

## Successful Response

Status:

```text
200 OK
```

Example:

```json
{
    "success": true,
    "data": {
        "access": "jwt_access_token",
        "refresh": "jwt_refresh_token"
    }
}
```

---

# Using Access Tokens

Authenticated requests require:

```http
Authorization: Bearer <access_token>
```

Example:

```http
GET /api/v1/profile/

Authorization: Bearer eyJhbGciOiJIUzI1...
```

---

# Refresh Token

## Endpoint

```http
POST /api/v1/auth/token/refresh/
```

## Description

Creates a new access token using a valid refresh token.

---

## Request Body

Example:

```json
{
    "refresh": "jwt_refresh_token"
}
```

---

## Successful Response

Status:

```text
200 OK
```

Example:

```json
{
    "access": "new_access_token"
}
```

---

# Logout

## Endpoint

```http
POST /api/v1/auth/logout/
```

## Description

Invalidates the current refresh token.

---

## Request Body

Example:

```json
{
    "refresh": "jwt_refresh_token"
}
```

---

## Successful Response

Status:

```text
200 OK
```

Example:

```json
{
    "success": true,
    "message": "Successfully logged out"
}
```

---

# Current User Profile

## Endpoint

```http
GET /api/v1/auth/profile/
```

## Description

Returns authenticated user information.

Requires:

```http
Authorization: Bearer <access_token>
```

---

## Successful Response

Example:

```json
{
    "success": true,
    "data": {
        "id": 1,
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "role": "customer"
    }
}
```

---

# Password Management

Future authentication features:

- Password recovery.
- Password reset.
- Email verification.
- Account activation.

---

# Authentication Errors

## Invalid Credentials

Status:

```text
401 Unauthorized
```

Example:

```json
{
    "success": false,
    "error": {
        "code": "invalid_credentials",
        "message": "Invalid email or password"
    }
}
```

---

## Expired Token

Status:

```text
401 Unauthorized
```

Solution:

Request a new access token using refresh token.

---

## Missing Token

Status:

```text
401 Unauthorized
```

Cause:

Protected endpoint accessed without authentication.

---

# Frontend Integration Notes

The frontend should implement:

- Authentication store.
- Token persistence.
- Axios interceptors.
- Automatic token refresh.
- Logout handling.
- Protected routes.

Recommended flow:

```text
Vue Router Guard

        |

Pinia Auth Store

        |

Axios Client

        |

JWT Authentication
```

---

# Security Considerations

The frontend should never:

- Trust user permissions locally.
- Store sensitive information.
- Expose refresh tokens unnecessarily.

The backend remains responsible for final authorization.

---

# Related Documentation

- API Overview
- Permissions API
- User API
- Backend Authentication Architecture
