# Inventory API Reference

## Overview

The Inventory application is responsible for managing product availability and stock levels.

This module is the single source of truth for inventory data.

Catalog displays products.

Inventory determines whether they are available for purchase.

---

# Responsibilities

The Inventory application manages:

- Stock levels
- Product availability
- Inventory validation
- Stock updates
- Inventory status

Business rules related to stock should remain isolated in this module.

---

# Base URL

```text
/api/v1/inventory/
```

---

# Main Resources

- Inventory
- Stock Movement
- Product Availability

---

# Available Endpoints

## Inventory

| Method | Endpoint | Authentication | Description |
|----------|---------------------------|---------------|------------------------------|
| GET | /products/ | Staff | Inventory list |
| GET | /products/<uuid>/ | Staff | Inventory detail |
| PATCH | /products/<uuid>/ | Staff/Admin | Update stock |

---

# Stock Information

Each inventory record maintains:

- Current stock
- Reserved stock
- Available stock
- Status

---

# Availability Rules

A product is considered available when:

- Product is active
- Product is visible
- Available stock is greater than zero

---

# Relationships

Inventory communicates with:

- Catalog
- Cart
- Orders

Inventory should never communicate directly with Payments.

---

# Frontend Integration

The storefront should display:

- In Stock
- Low Stock
- Out of Stock

Availability indicators should be updated using Inventory data.

---

# Related Documentation

- Catalog
- Cart
- Orders
