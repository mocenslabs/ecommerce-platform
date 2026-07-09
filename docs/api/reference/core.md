# Core API Reference

## Overview

The `core` application provides shared infrastructure used across the entire backend.

Rather than implementing business logic, it centralizes common functionality such as:

- Health checks
- Readiness probes
- Standard API responses
- Pagination
- Middleware
- Validators
- Exception handling
- Shared services
- Common utilities

This module acts as the foundation of the backend architecture.

---

# Responsibilities

The Core application is responsible for:

- Shared API infrastructure
- Request lifecycle utilities
- Consistent API responses
- Default pagination
- Health monitoring
- Middleware
- Global exception handling
- Reusable validators

Business logic is intentionally excluded from this module.

---

# Public Endpoints

Base path:

```text
/api/v1/core/
```

---

## Health Check

Endpoint

```http
GET /api/v1/core/health/
```

Authentication

```text
None
```

Permissions

```text
Public
```

Purpose

Returns the service liveness status.

Example response

```json
{
    "status": "healthy",
    "environment": "development"
}
```

---

## Readiness Check

Endpoint

```http
GET /api/v1/core/readiness/
```

Authentication

```text
None
```

Permissions

```text
Public
```

Purpose

Checks whether the application is ready to serve requests.

Current implementation validates:

- Database connectivity

Success response

```json
{
    "status": "ready"
}
```

Failure response

```json
{
    "status": "not_ready"
}
```

HTTP Status

```text
503 Service Unavailable
```

---

# Shared Components

## Pagination

Current default pagination:

```text
DefaultPagination
```

Configuration:

- page_size = 12
- page_size_query_param = "page_size"
- max_page_size = 100

---

## API Responses

The module provides standardized response helpers.

Success

```python
success_response(...)
```

Structure

```json
{
    "success": true,
    "message": "...",
    "data": {}
}
```

Error

```python
error_response(...)
```

Structure

```json
{
    "success": false,
    "message": "...",
    "errors": {}
}
```

---

# Validators

Current validators include:

- Password validation

Additional validators may be added as the platform evolves.

---

# Middleware

Current middleware:

- Request ID Middleware
- Performance Middleware

These components improve observability and diagnostics.

---

# Exception Handling

Global exception handling is centralized under:

```text
core/exceptions/
```

This ensures consistent error responses across the platform.

---

# Design Principles

Core should remain independent of business domains.

Business applications may depend on Core.

Core must never depend on business applications.

---

# Related Documentation

- Authentication
- API Error Handling
- Backend Architecture
