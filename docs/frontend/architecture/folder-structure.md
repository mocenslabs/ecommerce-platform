# Frontend Folder Structure

## Document Information

| Field         | Value                       |
|---------------|-----------------------------|
| Document Name | Frontend Folder Structure   |
| Version       | 1.0                         |
| Status        | Active                      |
| Area          | Frontend Engineering        |
| Scope         | Premium E-commerce Platform |
| Last Updated  | 2026-07-14                  |

---

# 1. Purpose

This document defines the physical organization of the frontend codebase.

The goal is to create a predictable structure where every file has a clear location and responsibility.

A good folder structure improves:

- maintainability;
- scalability;
- developer onboarding;
- code discoverability.

---

# 2. Organization Strategy

The frontend follows a hybrid architecture:

- Global shared resources.
- Feature-based modules.

Global resources contain reusable foundations.

Feature modules contain business-specific functionality.

---

# 3. Root Source Structure

The main source directory follows this structure:

src/
    |
    ├── app/
    ├── assets/
    ├── components/
    ├── composables/
    ├── layouts/
    ├── modules/
    ├── router/
    ├── services/
    ├── stores/
    ├── styles/
    ├── types/
    ├── utils/
    ├── views/
    └── main.ts


---

# 4. Folder Responsibilities

## app/

Application-level configuration.

Contains:

- initialization logic;
- global providers;
- application setup.

---

## assets/

Static resources.

Examples:

- images;
- fonts;
- icons;
- media files.

---

## components/

Global reusable components.

These components should not contain business-specific logic.

Examples:

- UI elements;
- design system components;
- shared layouts.

---

## composables/

Global reusable logic.

Examples:

- browser interactions;
- shared state logic;
- reusable behaviors.

---

## layouts/

Application layouts.

Examples:

- MainLayout;
- AuthLayout;
- DashboardLayout.

Layouts define page structure.

---

## modules/

Business feature modules.

Each module represents a specific domain.

Examples:

    modules/

    authentication/

    catalog/

    cart/

    checkout/

    orders/

    wishlist/

    profile/


---

# 5. Module Structure

A feature module should follow this pattern:

module-name/

            ├── components/
            ├── composables/
            ├── services/
            ├── stores/
            ├── types/
            ├── utils/
            └── index.ts


Not every module requires every folder.

Only create what is necessary.

---

# 6. router/

Application routing configuration.

Responsible for:

- routes;
- navigation rules;
- route guards.

---

# 7. services/

Global external communication.

Examples:

- API client;
- authentication client;
- shared integrations.

Business-specific services should remain inside their modules.

---

# 8. stores/

Global application state.

Examples:

- application configuration;
- user session;
- global preferences.

Feature-specific stores belong inside modules.

---

# 9. styles/

Global styling system.

Contains:

- design tokens;
- CSS variables;
- global styles;
- themes;
- animations.

No component-specific styles should be placed here.

---

# 10. types/

Global TypeScript definitions.

Examples:

- shared interfaces;
- common types;
- API contracts.

Feature-specific types belong inside modules.

---

# 11. utils/

Pure reusable helper functions.

Utilities should:

- be independent;
- have no business logic;
- be easily testable.

---

# 12. views/

Application pages.

Views should compose:

- layouts;
- components;
- modules.

Complex business logic should not live here.

---

# 13. File Organization Rules

The following rules apply:

## Rule 1

Do not create folders without a clear responsibility.

## Rule 2

Do not place business logic inside global folders.

## Rule 3

Avoid giant files.

## Rule 4

Prefer local ownership of features.

## Rule 5

Shared code must prove that it is truly shared.

---

# 14. Scalability Considerations

This structure allows the application to grow by adding modules.

Example:

    Future:

        modules/

        marketing/

        subscriptions/

        analytics/

        notifications/


without affecting existing domains.

---

# Related Documents

- Frontend Architecture Overview
- Data Flow
- State Management
- API Layer
- Coding Standards

---

# Document Status

Status: Active

Version: 1.0
