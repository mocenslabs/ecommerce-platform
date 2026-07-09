# Payments API Reference

## Overview

The Payments application is responsible for processing, tracking and managing payment transactions.

It acts as an abstraction layer between the ecommerce platform and external payment providers.

The application never creates orders.

It only processes payments for existing orders.

---

# Responsibilities

The Payments application manages:

- Payment creation
- Payment confirmation
- Payment status
- Payment provider integration
- Transaction tracking
- Refund support (future)

---

# Base URL

```text
/api/v1/payments/
```

---

# Main Resources

- Payment
- Payment Transaction

---

# Available Endpoints

## Payments

| Method | Endpoint | Authentication | Description |
|----------|----------------------------|---------------|-----------------------------|
| POST | /create/ | JWT | Create payment |
| GET | /<uuid>/ | JWT | Payment detail |
| POST | /webhook/ | Public (Signed) | Payment provider callback |

---

# Payment Flow

Order

↓

Payment Created

↓

External Provider

↓

Confirmation

↓

Order Updated

↓

Notification

---

# Payment Status

Typical states:

- Pending
- Processing
- Authorized
- Paid
- Failed
- Cancelled
- Refunded

---

# Relationships

Payments communicate with:

- Orders
- Notifications

Payments should not communicate directly with:

- Catalog
- Inventory
- Wishlist

---

# Security

Payment requests must always be authenticated.

Webhook endpoints must validate provider signatures.

Sensitive payment information must never be stored.

---

# Frontend Integration

Frontend responsibilities:

- Initiate payment
- Display payment status
- Poll or receive confirmation
- Redirect after success/failure

Payment validation always occurs on the backend.

---

# Related Documentation

- Orders
- Notifications
- Security
