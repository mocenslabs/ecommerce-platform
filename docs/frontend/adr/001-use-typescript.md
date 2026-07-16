# ADR-001 — Use TypeScript

## Status

Accepted

---

## Date

2026-07-14

---

## Context

The frontend application requires a scalable and maintainable codebase.

As the project grows, stronger type safety becomes essential to reduce runtime errors, improve tooling, and facilitate collaboration.

The previous frontend version was developed using JavaScript, which provided flexibility but allowed type-related issues to appear later in the development process.

---

## Decision

The frontend will be developed using TypeScript.

TypeScript becomes the official language for all new frontend development.

JavaScript files should only exist when strictly required by third-party tooling.

---

## Alternatives Considered

### JavaScript

Advantages:

- simpler syntax;
- no compilation step.

Reasons for rejection:

- weaker type safety;
- lower maintainability in large applications;
- reduced IDE support.

---

## Consequences

Positive:

- safer refactoring;
- better autocomplete;
- improved documentation through types;
- earlier error detection.

Negative:

- initial learning curve;
- additional type definitions.

Trade-offs:

- slightly increased complexity in exchange for significantly improved maintainability.

---

## Implementation Notes

TypeScript configuration should enforce strict mode whenever practical.

New source files should use the `.ts` or `.vue` format with TypeScript support.

---

## Related Documents

- Technology Stack
- Frontend Constitution
- Workspace Overview

---

## Status History

| Date | Status | Notes |
|------|--------|------|
| 2026-07-14 | Accepted | Initial decision |
