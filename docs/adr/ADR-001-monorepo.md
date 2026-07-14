# ADR-001: Monorepo Architecture

## Status

Accepted

---

## Context

The project contains multiple components:

- Backend API
- Frontend
- Documentation
- Infrastructure
- CI/CD

Managing them across multiple repositories would increase coordination complexity.

---

## Decision

Use a single monorepo to host all project components.

---

## Consequences

### Positive

- Single source of truth
- Simplified dependency management
- Easier documentation
- Unified CI/CD
- Atomic commits across backend and frontend

### Negative

- Larger repository
- Requires clear directory organization
