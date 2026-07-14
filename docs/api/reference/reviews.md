# Reviews API Reference

## Overview

The Reviews application manages customer feedback and product ratings.

It allows authenticated users to submit reviews for products and provides aggregated rating information for the catalog.

---

# Responsibilities

- Product reviews
- Product ratings
- Review moderation
- Review visibility

---

# Base URL

/api/v1/reviews/

---

# Main Resources

- Review
- Rating

---

# Relationships

- Users
- Catalog

---

# Business Rules

- Only authenticated users may submit reviews.
- Reviews belong to a single user.
- Reviews belong to a single product.
- Ratings are calculated from published reviews.

---

# Frontend Integration Notes

Frontend should:

- Display average rating.
- Paginate reviews.
- Allow editing only by the review owner.
- Refresh ratings after review submission.
