# Domain Model

## Overview

This document describes the core business entities of the ecommerce platform, their responsibilities, relationships, and ownership.

---

# User

## Responsibility

Represents a registered customer or administrator.

## Owned By

Users application

## Relationships

- Orders
- Wishlist
- Reviews
- Notifications

---

# Product

## Responsibility

Represents an item available for sale.

## Owned By

Catalog

## Relationships

- Category
- Brand
- Inventory
- Reviews

---

# Category

Groups products.

Owned by Catalog.

---

# Brand

Represents the manufacturer or product brand.

Owned by Catalog.

---

# Inventory

Represents stock information.

Owned by Inventory.

Never stores product metadata.

---

# Cart

Temporary purchase container.

Owned by Cart.

---

# Cart Item

Represents one product inside a cart.

---

# Order

Represents a finalized purchase.

Owned by Orders.

Immutable after confirmation.

---

# Order Item

Snapshot of purchased products.

Never references mutable catalog data.

---

# Payment

Represents a financial transaction.

Owned by Payments.

---

# Coupon

Represents a promotional rule.

Owned by Discounts.

---

# Review

Represents customer feedback.

Owned by Reviews.

---

# Notification

Represents a system-generated message.

Owned by Notifications.

---

# Audit Log

Represents an immutable audit event.

Owned by Audit.
