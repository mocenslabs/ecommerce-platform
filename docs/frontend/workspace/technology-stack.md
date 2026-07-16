# Frontend Technology Stack

## Document Information

| Field | Value |
|---|---|
| Document Name | Frontend Technology Stack |
| Version | 1.0 |
| Status | Active |
| Area | Frontend Engineering |
| Scope | Premium E-commerce Platform |
| Last Updated | 2026-07-14 |

---

# 1. Purpose

This document defines the official technology stack used by the frontend application.

Its objective is to establish a consistent and maintainable development environment by documenting approved technologies and their responsibilities.

---

# 2. Technology Selection Philosophy

Technologies are selected based on:

- long-term maintenance;
- community adoption;
- documentation quality;
- ecosystem maturity;
- performance;
- developer experience.

New technologies should only be introduced when they provide clear value.

---

# 3. Core Technologies

These technologies form the foundation of the frontend application.

| Category | Technology | Status |
|----------|------------|--------|
| Framework | Vue 3 | Official |
| Language | TypeScript | Official |
| Build Tool | Vite | Official |
| Styling | Tailwind CSS v4 | Official |
| Routing | Vue Router | Official |
| State Management | Pinia | Official |
| HTTP Client | Axios | Official |
| Internationalization | Vue I18n | Official |

---

# 4. UI Foundation

The visual layer is built using the project's Design System.

Official libraries:

| Category | Technology | Status |
|----------|------------|--------|
| Icons | Lucide Vue Next | Official |
| Design Tokens | Internal | Official |

No external UI framework will be used.

Reusable components are developed internally.

---

# 5. Form Management

Official libraries:

| Category | Technology | Status |
|----------|------------|--------|
| Forms | VeeValidate | Official |
| Validation | Zod | Official |

Validation schemas should be shared whenever possible.

---

# 6. Data Visualization

Official library:

| Category | Technology | Status |
|----------|------------|--------|
| Charts | Apache ECharts | Official |

Charts should be encapsulated inside reusable components.

---

# 7. Tables

Official library:

| Category | Technology | Status |
|----------|------------|--------|
| Data Tables | TanStack Table | Official |

Business logic should remain outside table implementations.

---

# 8. Testing Stack

Testing follows multiple layers.

| Category | Technology | Status |
|----------|------------|--------|
| Unit Testing | Vitest | Official |
| Component Testing | Vue Test Utils | Official |
| End-to-End Testing | Playwright | Official |

---

# 9. Code Quality

Official tools:

| Category | Technology | Status |
|----------|------------|--------|
| Linting | ESLint | Official |
| Formatting | Prettier | Official |
| CSS Linting | Stylelint | Official |

Formatting should be automated.

---

# 10. Git Automation

Official tools:

| Category | Technology | Status |
|----------|------------|--------|
| Git Hooks | Husky | Official |
| Commit Validation | Commitlint | Official |
| Staged Files | lint-staged | Official |

Every commit should pass automated quality checks.

---

# 11. Package Management

Official package manager:

```text
npm
```

Package management should remain consistent across the project.

---

# 12. Technologies Explicitly Not Used

The following technologies are outside the project's scope.

Examples:

- Vuex
- Bootstrap
- Vuetify
- Element Plus
- jQuery

Introducing alternative technologies requires architectural review.

---

# 13. Evaluation Criteria

Future technologies should be evaluated according to:

- maintenance status;
- ecosystem compatibility;
- documentation;
- performance;
- accessibility;
- community adoption.

---

# 14. Benefits

A documented technology stack provides:

- consistent development;
- easier onboarding;
- predictable architecture;
- simpler maintenance;
- reduced technical debt.

---

# Related Documents

- Workspace Overview
- Installation Guide
- Code Quality
- Development Workflow
- Frontend Constitution

---

# Document Status

Status: Active

Version: 1.0
