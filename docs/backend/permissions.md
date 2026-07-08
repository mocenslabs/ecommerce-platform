# Permissions Architecture

## Introduction

The **Premium E-commerce Platform** uses a permission-based authorization system to control access to resources and operations.

Authentication identifies users.

Authorization determines what authenticated users are allowed to do.

Both mechanisms work together to protect the platform.

---

# Authentication vs Authorization

## Authentication

Answers:

> Who is the user?

Example:

```text
User logs in

↓

Identity verification

↓

JWT token issued
```

---

## Authorization

Answers:

> What can the user do?

Example:

```text
Authenticated User

↓

Permission Check

↓

Allowed Action
```

---

# Permission Strategy

The platform follows these principles:

- Default deny access.
- Explicit permission definitions.
- Least privilege.
- Domain ownership.
- Consistent enforcement.

---

# Permission Levels

The system defines multiple access levels.

---

# Public Access

Available without authentication.

Examples:

```text
Product listing

Category browsing

Public information
```

Purpose:

Allow users to explore the platform before creating an account.

---

# Customer Permissions

Regular authenticated users.

Allowed actions:

```text
View profile

Manage cart

Manage wishlist

Create orders

View order history

Submit reviews
```

Restrictions:

```text
Cannot access administration features.

Cannot modify other users.

Cannot modify system configuration.
```

---

# Staff Permissions

Operational users.

Possible permissions:

```text
Manage products

Manage inventory

Review orders

Handle customer operations
```

Staff permissions should be limited according to their responsibilities.

---

# Administrator Permissions

Full management access.

Capabilities:

```text
Manage users

Manage permissions

Configure system settings

Access reports

Manage all resources
```

Administrative actions should be audited.

---

# Django REST Framework Permissions

API endpoints should explicitly define required permissions.

Example:

```python
permission_classes = [
    IsAuthenticated
]
```

or:

```python
permission_classes = [
    IsAdminUser
]
```

---

# Endpoint Access Model

General classification:

---

## Public Endpoints

Examples:

```text
GET /api/products/

GET /api/categories/
```

---

## Authenticated Endpoints

Examples:

```text
GET /api/profile/

POST /api/orders/

GET /api/wishlist/
```

---

## Administrative Endpoints

Examples:

```text
POST /api/dashboard/

PATCH /api/users/{id}/
```

---

# Object-Level Permissions

Some operations require checking ownership.

Examples:

A customer can:

```text
View own orders
```

but cannot:

```text
View another customer's orders
```

---

# Resource Ownership Rules

Examples:

## Cart

Users can only access:

```text
their own cart
```

---

## Wishlist

Users can only manage:

```text
their own wishlist items
```

---

## Orders

Users can only access:

```text
their own order history
```

---

## Reviews

Users can manage:

```text
their own reviews
```

---

# Administrative Security

Administrative operations should include:

- Permission validation.
- Audit logging.
- Restricted access.
- Secure configuration.

Sensitive actions should always be traceable.

---

# Permission Implementation Guidelines

Permissions should:

- Be reusable.
- Avoid duplicated logic.
- Remain close to business rules.
- Be tested independently.

---

# Permission Errors

Common authorization errors:

## 401 Unauthorized

Meaning:

The user is not authenticated.

Example:

```text
Missing JWT token
```

---

## 403 Forbidden

Meaning:

The user is authenticated but lacks permission.

Example:

```text
Customer accessing admin endpoint
```

---

# Security Considerations

The system should avoid:

- Trusting frontend restrictions.
- Exposing sensitive data.
- Relying only on UI permissions.
- Missing backend validation.

The backend is always the final authority.

---

# Future Improvements

Possible enhancements:

- Fine-grained permission management.
- Dynamic roles.
- Organization-based permissions.
- Advanced access policies.

---

# Related Documentation

- Authentication Architecture
- Security Policy
- Backend Applications
- API Documentation
- Business Rules
