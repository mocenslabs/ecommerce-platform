# API Endpoint Reference

## Introduction

This document provides a complete overview of the REST API endpoints available in the **Premium E-commerce Platform**.

The API follows a resource-oriented architecture.

Base URL:

```text
/api/v1/
```

---

# Endpoint Structure

General format:

```text
/api/v1/{resource}/
```

Example:

```text
/api/v1/products/
```

---

# Authentication

Endpoints marked as:

```text
Public
```

do not require authentication.

Endpoints marked as:

```text
Authenticated
```

require:

```http
Authorization: Bearer <access_token>
```

---

# Authentication

Base path:

```text
/api/v1/auth/
```

| Method | Endpoint | Access | Description |
|---|---|---|---|
| POST | `/auth/register/` | Public | Create account |
| POST | `/auth/login/` | Public | Authenticate user |
| POST | `/auth/token/refresh/` | Public | Refresh access token |
| POST | `/auth/logout/` | Authenticated | Logout user |
| GET | `/auth/profile/` | Authenticated | Get current user |

---

# Users

Base path:

```text
/api/v1/users/
```

Responsible application:

```text
users
```

---

## User Profile

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/users/profile/` | Authenticated | Retrieve profile |
| PATCH | `/users/profile/` | Authenticated | Update profile |

---

# Catalog

Base path:

```text
/api/v1/catalog/
```

Responsible applications:

```text
catalog
```

---

# Products

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/products/` | Public | List products |
| GET | `/products/{id}/` | Public | Product detail |
| POST | `/products/` | Admin | Create product |
| PATCH | `/products/{id}/` | Admin | Update product |
| DELETE | `/products/{id}/` | Admin | Delete product |

---

# Categories

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/categories/` | Public | List categories |
| GET | `/categories/{id}/` | Public | Category detail |
| POST | `/categories/` | Admin | Create category |

---

# Cart

Base path:

```text
/api/v1/cart/
```

Responsible application:

```text
cart
```

---

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/cart/` | Authenticated | Get current cart |
| POST | `/cart/items/` | Authenticated | Add item |
| PATCH | `/cart/items/{id}/` | Authenticated | Update quantity |
| DELETE | `/cart/items/{id}/` | Authenticated | Remove item |

---

# Wishlist

Base path:

```text
/api/v1/wishlist/
```

Responsible application:

```text
wishlist
```

---

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/wishlist/` | Authenticated | List wishlist |
| POST | `/wishlist/items/` | Authenticated | Add product |
| DELETE | `/wishlist/items/{id}/` | Authenticated | Remove product |

---

# Orders

Base path:

```text
/api/v1/orders/
```

Responsible application:

```text
orders
```

---

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/orders/` | Authenticated | User orders |
| GET | `/orders/{id}/` | Authenticated | Order detail |
| POST | `/orders/` | Authenticated | Create order |

---

# Payments

Base path:

```text
/api/v1/payments/
```

Responsible application:

```text
payments
```

---

| Method | Endpoint | Access | Description |
|---|---|---|---|
| POST | `/payments/create/` | Authenticated | Create payment |
| GET | `/payments/{id}/` | Authenticated | Payment detail |

---

# Reviews

Base path:

```text
/api/v1/reviews/
```

Responsible application:

```text
reviews
```

---

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/reviews/` | Public | List reviews |
| POST | `/reviews/` | Authenticated | Create review |
| PATCH | `/reviews/{id}/` | Owner | Update review |
| DELETE | `/reviews/{id}/` | Owner | Delete review |

---

# Inventory

Base path:

```text
/api/v1/inventory/
```

Responsible application:

```text
inventory
```

---

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/inventory/{product}/` | Admin | Check stock |
| PATCH | `/inventory/{product}/` | Admin | Update stock |

---

# Discounts

Base path:

```text
/api/v1/discounts/
```

Responsible application:

```text
discounts
```

---

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/discounts/validate/` | Authenticated | Validate coupon |
| POST | `/discounts/` | Admin | Create discount |

---

# Notifications

Base path:

```text
/api/v1/notifications/
```

Responsible application:

```text
notifications
```

---

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/notifications/` | Authenticated | List notifications |
| PATCH | `/notifications/{id}/read/` | Authenticated | Mark as read |

---

# Dashboard

Base path:

```text
/api/v1/dashboard/
```

Responsible application:

```text
dashboard
```

---

| Method | Endpoint | Access | Description |
|---|---|---|---|
| GET | `/dashboard/statistics/` | Admin | Platform metrics |

---

# Endpoint Design Rules

All endpoints should:

- Use consistent naming.
- Return predictable responses.
- Validate permissions.
- Follow REST principles.

---

# Future API Modules

Possible future resources:

```text
/api/v1/search/

/api/v1/recommendations/

/api/v1/reports/

/api/v1/integrations/
```

---

# Related Documentation

- API Overview
- Authentication API
- Error Handling
- Pagination
- Filtering
- Backend Applications
