# Frontend Integration Guide

## Overview

This document describes the recommended order for consuming backend services.

---

# Startup Flow

Application

↓

Refresh Token

↓

Authentication

↓

Current User

↓

Catalog

---

# Product Page

Catalog

↓

Inventory

↓

Reviews

↓

Wishlist Status

---

# Checkout

Cart

↓

Discount Validation

↓

Inventory Validation

↓

Order Creation

↓

Payment

↓

Confirmation

---

# Error Handling

Frontend should gracefully handle:

- Unauthorized
- Forbidden
- Validation errors
- Network failures
- Timeouts

---

# Caching

Recommended cache:

Catalog

Categories

Brands

Current User

Notification Count
