# API Pagination

## Introduction

The **Premium E-commerce Platform API** uses pagination to efficiently handle large collections of resources.

Pagination improves:

- API performance.
- Database efficiency.
- Frontend rendering.
- User experience.

---

# Pagination Strategy

The API uses page-based pagination.

General format:

```text
?page={number}
```

Example:

```http
GET /api/v1/products/?page=2
```

---

# Default Pagination

Collections return a limited number of records per request.

Example:

```text
Page 1

Products 1-20
```

```text
Page 2

Products 21-40
```

---

# Pagination Parameters

## Page

Defines the requested page.

Example:

```http
?page=3
```

---

## Page Size

Defines the number of items returned.

Example:

```http
?page_size=50
```

The maximum allowed page size should be limited to prevent excessive queries.

---

# Response Format

Paginated responses follow a consistent structure.

Example:

```json
{
    "count": 150,
    "next": "/api/v1/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Product Example"
        }
    ]
}
```

---

# Response Fields

## count

Total number of available records.

Example:

```json
150
```

---

## next

URL for the next page.

Example:

```text
/api/v1/products/?page=2
```

Returns:

```text
null
```

when no next page exists.

---

## previous

URL for the previous page.

Example:

```text
/api/v1/products/?page=1
```

Returns:

```text
null
```

on the first page.

---

## results

Contains the current page data.

Example:

```json
[
    {
        "id": 1,
        "name": "Laptop"
    }
]
```

---

# Paginated Resources

Common resources requiring pagination:

## Products

Example:

```http
GET /api/v1/products/
```

---

## Orders

Example:

```http
GET /api/v1/orders/
```

---

## Reviews

Example:

```http
GET /api/v1/reviews/
```

---

## Notifications

Example:

```http
GET /api/v1/notifications/
```

---

# Resources Without Pagination

Small collections may not require pagination.

Examples:

- Static configuration.
- Small enumerations.
- Fixed choices.

---

# Frontend Integration

Frontend applications should:

- Load data page by page.
- Avoid requesting unnecessary records.
- Handle loading states.
- Provide navigation controls.

Example flow:

```text
User Opens Catalog

        |

Request Page 1

        |

Display Products

        |

User Changes Page

        |

Request Page 2
```

---

# Infinite Scroll Support

The pagination structure allows future support for:

- Infinite scrolling.
- Lazy loading.
- Progressive rendering.

Example:

```text
Load first products

↓

User scrolls

↓

Request next page
```

---

# Performance Considerations

Pagination reduces:

- Database load.
- Response size.
- Memory usage.
- Frontend rendering cost.

---

# Security Considerations

Pagination limits should prevent:

- Excessive data extraction.
- Large uncontrolled responses.
- Performance abuse.

---

# Pagination Errors

Possible errors:

## Invalid Page

Example:

```text
?page=999999
```

Response:

```json
{
    "success": false,
    "error": {
        "code": "invalid_page",
        "message": "Invalid page number"
    }
}
```

---

# Future Improvements

Possible enhancements:

- Cursor pagination.
- Advanced search pagination.
- Personalized ordering.
- Optimized catalog queries.

---

# Related Documentation

- API Overview
- Filtering
- Endpoint Reference
- Frontend Integration Guide
- Database Architecture
