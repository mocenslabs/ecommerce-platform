# Wishlist API Reference

## Overview

The Wishlist application allows authenticated users to save products for future purchases.

It provides a persistent collection of products independent of the shopping cart.

Wishlist data belongs to the authenticated user and is not shared.

---

# Responsibilities

The Wishlist application manages:

- Wishlist creation
- Wishlist items
- Product persistence
- Product removal
- Wishlist retrieval

---

# Base URL

```text
/api/v1/wishlist/
```

---

# Main Resources

- Wishlist
- WishlistItem

---

# Available Endpoints

## Wishlist

| Method | Endpoint | Authentication | Description |
|----------|-------------------------|---------------|------------------------------|
| GET | / | JWT | Retrieve current wishlist |
| DELETE | /clear/ | JWT | Remove all wishlist items |

---

## Wishlist Items

| Method | Endpoint | Authentication | Description |
|----------|-------------------------------|---------------|-----------------------------|
| POST | /items/ | JWT | Add product |
| DELETE | /items/<uuid>/delete/ | JWT | Remove product |

---

# Business Rules

Users may only manage their own wishlist.

Products may exist in the wishlist even if they become unavailable.

Wishlist does not reserve stock.

---

# Relationships

Wishlist communicates with:

- Users
- Catalog

Wishlist does not modify:

- Inventory
- Orders
- Payments

---

# Frontend Integration

Typical frontend components:

- Wishlist page
- Product detail
- Product cards
- Header counter

---

# Related Documentation

- Catalog
- Cart
- Users
