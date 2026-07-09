# Cart API Reference

## Overview

The Cart application manages the shopping cart lifecycle before checkout.

It allows authenticated users to create, update and manage their shopping cart independently from the order process.

The cart represents a temporary collection of products that may later become an order.

---

# Responsibilities

The Cart application manages:

- Shopping carts
- Cart items
- Product quantities
- Cart totals
- Cart validation

---

# Base URL

```text
/api/v1/cart/
```

---

# Main Resources

- Cart
- CartItem

---

# Available Endpoints

## Cart

| Method | Endpoint | Authentication | Description |
|----------|---------------------------|---------------|-----------------------------|
| GET | / | JWT | Retrieve current cart |
| DELETE | /clear/ | JWT | Empty cart |

---

## Cart Items

| Method | Endpoint | Authentication | Description |
|----------|----------------------------------|---------------|----------------------------|
| POST | /items/ | JWT | Add item |
| PATCH | /items/<uuid>/ | JWT | Update quantity |
| DELETE | /items/<uuid>/delete/ | JWT | Remove item |

---

# Business Rules

The Cart module validates:

- Product existence
- Product availability
- Requested quantity
- Inventory availability

---

# Relationships

Cart communicates with:

- Users
- Catalog
- Inventory

The Cart application does not process payments.

---

# Checkout

Checkout transfers validated cart data to the Orders application.

After successful order creation the cart may be cleared.

---

# Frontend Integration

Primary frontend consumers:

- Mini cart
- Cart page
- Checkout
- Navbar cart badge

---

# Related Documentation

- Inventory
- Orders
- Catalog
