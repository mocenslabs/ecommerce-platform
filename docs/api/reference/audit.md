# Audit API Reference

## Overview

The Audit application records relevant system events for traceability and compliance.

---

# Responsibilities

- User actions
- Administrative actions
- Authentication events
- Data changes

---

# Relationships

Every application may emit audit events.

Audit never modifies business data.

---

# Frontend Integration Notes

Administrative use only.

Suggested filters:

- User
- Date
- Resource
- Event type
