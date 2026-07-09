# Orders API Reference

## Overview

The Orders application manages the complete order lifecycle.

It is responsible for transforming a validated shopping cart into a persistent order and tracking its progress until completion.

Orders are immutable business records and represent the official purchase transaction.

---

# Responsibilities

The Orders application manages:

- Order creation
- Order items
- Order status
- Customer order history
- Order validation

Payment processing is handled by the Payments application.

---

# Base URL

```text
/api/v1/orders/
```

---

# Main Resources

- Order
- OrderItem

---

# Available Endpoints

## Orders

| Method | Endpoint | Authentication | Description |
|----------|---------------------------|---------------|-----------------------------|
| GET | / | JWT | List customer orders |
| POST | / | JWT | Create order |
| GET | /<uuid>/ | JWT | Order detail |
| PATCH | /<uuid>/ | Staff/Admin | Update order status |

---

# Order Creation

Order creation requires:

- Authenticated user
- Valid cart
- Available inventory

The system validates the cart before creating an order.

---

# Order States

Possible states include:

- Pending
- Confirmed
- Paid
- Processing
- Shipped
- Delivered
- Cancelled

---

# Relationships

Orders communicate with:

- Users
- Cart
- Inventory
- Payments
- Notifications

---

# Business Rules

Orders are immutable after payment.

Inventory validation occurs before order creation.

Each order belongs to a single customer.

---

# Frontend Integration

Typical frontend pages:

- Checkout
- Order confirmation
- Order history
- Order detail
- Customer dashboard

---

# Related Documentation

- Cart
- Inventory
- Payments
