# API Examples

## Introduction

This document provides practical examples of how clients interact with the **Premium E-commerce Platform API**.

Examples are intended for:

- Frontend developers.
- API consumers.
- Testing purposes.
- Integration development.

Base URL:

```text
/api/v1/
```

---

# Authentication Example

## Login

Endpoint:

```http
POST /api/v1/auth/login/
```

Request:

```json
{
    "email": "customer@example.com",
    "password": "secure_password"
}
```

Response:

```json
{
    "success": true,
    "data": {
        "access": "access_token",
        "refresh": "refresh_token"
    }
}
```

---

# Authenticated Request

Example:

```http
GET /api/v1/auth/profile/
```

Headers:

```http
Authorization: Bearer access_token
```

Response:

```json
{
    "success": true,
    "data": {
        "id": 1,
        "email": "customer@example.com",
        "role": "customer"
    }
}
```

---

# Product Catalog Example

## List Products

Request:

```http
GET /api/v1/products/
```

Response:

```json
{
    "count": 2,
    "results": [
        {
            "id": 1,
            "name": "Laptop",
            "price": 1200
        },
        {
            "id": 2,
            "name": "Keyboard",
            "price": 80
        }
    ]
}
```

---

# Product Detail Example

Request:

```http
GET /api/v1/products/1/
```

Response:

```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "Laptop",
        "description": "Professional laptop",
        "price": 1200,
        "stock": 15
    }
}
```

---

# Search Example

Request:

```http
GET /api/v1/products/?search=laptop
```

Response:

```json
{
    "count": 1,
    "results": [
        {
            "id": 1,
            "name": "Laptop"
        }
    ]
}
```

---

# Cart Examples

## Get Current Cart

Request:

```http
GET /api/v1/cart/
```

Headers:

```http
Authorization: Bearer access_token
```

Response:

```json
{
    "items": [
        {
            "product": 1,
            "quantity": 2,
            "subtotal": 2400
        }
    ],
    "total": 2400
}
```

---

## Add Item To Cart

Request:

```http
POST /api/v1/cart/items/
```

Body:

```json
{
    "product_id": 1,
    "quantity": 2
}
```

Response:

```json
{
    "success": true,
    "message": "Product added to cart"
}
```

---

# Order Example

## Create Order

Request:

```http
POST /api/v1/orders/
```

Body:

```json
{
    "shipping_address": 5,
    "payment_method": "card"
}
```

Response:

```json
{
    "success": true,
    "data": {
        "id": 1001,
        "status": "pending",
        "total": 2400
    }
}
```

---

# Order Detail

Request:

```http
GET /api/v1/orders/1001/
```

Response:

```json
{
    "id": 1001,
    "status": "confirmed",
    "items": [
        {
            "product": "Laptop",
            "quantity": 2
        }
    ]
}
```

---

# Payment Example

## Create Payment

Request:

```http
POST /api/v1/payments/create/
```

Body:

```json
{
    "order_id": 1001,
    "method": "card"
}
```

Response:

```json
{
    "success": true,
    "data": {
        "payment_id": 5001,
        "status": "pending"
    }
}
```

---

# Error Example

Request:

```http
POST /api/v1/orders/
```

Invalid stock example:

Response:

```json
{
    "success": false,
    "error": {
        "code": "insufficient_stock",
        "message": "Product is not available"
    }
}
```

---

# Frontend Service Example

A frontend service layer should abstract API communication.

Example:

```text
src/

services/

├── auth.service.js

├── product.service.js

├── cart.service.js

└── order.service.js
```

---

# Axios Request Flow

General architecture:

```text
Vue Component

        |

Pinia Store

        |

Service Layer

        |

Axios Client

        |

API Endpoint
```

---

# Testing Examples

API examples can be used with:

- Swagger UI.
- Postman.
- Automated tests.
- Frontend development.

---

# Future Improvements

Possible additions:

- Complete OpenAPI examples.
- Generated SDK clients.
- Interactive documentation.
- Integration tests.

---

# Related Documentation

- API Overview
- Authentication API
- Endpoint Reference
- Error Handling
- Frontend Integration Guide
