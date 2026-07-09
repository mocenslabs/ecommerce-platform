# Catalog API Reference

## Overview

The Catalog application is responsible for exposing all product-related information to the platform.

It provides the public product catalog, category navigation, product details and catalog management endpoints.

This module acts as the primary data source for the storefront.

---

# Responsibilities

The Catalog application manages:

- Products
- Categories
- Brands
- Product Images
- Product Metadata
- Product Visibility

---

# Base URL

```text
/api/v1/catalog/
```

---

# Main Resources

- Product
- Category
- Brand
- ProductImage

---

# Available Endpoints

## Products

| Method | Endpoint | Authentication | Description |
|----------|-----------------------------|---------------|----------------------------|
| GET | /products/ | Public | List products |
| GET | /products/<slug>/ | Public | Product detail |
| POST | /products/ | Admin | Create product |
| PATCH | /products/<uuid>/ | Admin | Update product |
| DELETE | /products/<uuid>/ | Admin | Delete product |

---

## Categories

| Method | Endpoint |
|----------|----------------|
| GET | /categories/ |
| GET | /categories/<slug>/ |

---

## Brands

| Method | Endpoint |
|----------|----------------|
| GET | /brands/ |
| GET | /brands/<slug>/ |

---

# Product Detail

The product endpoint returns information including:

- Basic information
- Pricing
- Images
- Brand
- Category
- Availability
- Visibility

Inventory information is supplied by the Inventory application.

---

# Search

Supported search fields include:

- Product name
- SKU
- Slug

---

# Filtering

Products may be filtered by:

- Category
- Brand
- Active status
- Featured products

---

# Ordering

Supported ordering includes:

- Name
- Price
- Creation date

---

# Pagination

Default pagination is provided by the Core application.

---

# Permissions

Public:

- View catalog

Administrators:

- Create products
- Update products
- Delete products

---

# Relationships

Catalog communicates with:

- Inventory
- Reviews
- Cart
- Wishlist
- Orders

---

# Frontend Integration

The Catalog module is the primary source of data for:

- Home page
- Product listing
- Product detail page
- Search page
- Category pages
- Brand pages

---

# Related Documentation

- Inventory
- Reviews
- Cart
- Orders
