# OpenAPI Documentation Guide

## Purpose

This document explains how API documentation is generated and maintained.

---

# Tool

The project uses:

- Django REST Framework
- DRF Spectacular

---

# Documentation Endpoints

Swagger UI

```text
/api/schema/swagger-ui/
```

Redoc

```text
/api/schema/redoc/
```

OpenAPI Schema

```text
/api/schema/
```

---

# Best Practices

Every endpoint should define:

- Serializer
- Request body
- Response body
- Status codes
- Authentication
- Permissions

---

# Documentation Rules

Whenever an endpoint changes:

- Update serializers.
- Update schema annotations.
- Review generated documentation.

---

# Versioning

Documentation follows API versioning.

Example:

/api/v1/

Future versions:

/api/v2/

---

# Release Checklist

Before every release:

- Regenerate schema.
- Verify Swagger.
- Verify Redoc.
