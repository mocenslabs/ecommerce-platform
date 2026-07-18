# CSS Architecture

---

## Document Information

| Property | Value |
|----------|-------|
| Version | 1.0.0 |
| Status | Approved |
| Last Updated | 2026-07-17 |
| Author | Mocens Labs |
| Audience | Frontend Developers, Software Architects, Contributors |

---

# 1. Purpose

This document defines the official CSS architecture of the Premium E-commerce Platform.

Its objective is to establish clear architectural boundaries between styling layers, ensuring scalability, maintainability and long-term consistency.

Every stylesheet within the project must follow this architecture.

---

# 2. Architecture Philosophy

The CSS architecture follows a layered approach.

Each layer has a single responsibility.

Higher layers may consume lower layers.

Lower layers must never depend on higher layers.

This dependency direction guarantees loose coupling and simplifies maintenance.

---

# 3. Layer Overview

The frontend styling architecture is organized as follows.

```
Foundation Layer
        │
        ▼
Theme Layer
        │
        ▼
Semantic Layer
        │
        ▼
Utilities
        │
        ▼
Base Components
        │
        ▼
Composite Components
        │
        ▼
Layouts
        │
        ▼
Pages
```

Each layer exists for a specific purpose.

---

# 4. Foundation Layer

The Foundation Layer provides the primitive building blocks of the Design System.

It defines values only.

It never defines appearance or component behavior.

Current Foundation Tokens include:

- Colors
- Spacing
- Typography
- Radius
- Elevation
- Motion
- Breakpoints
- Z-Index

Foundation Tokens are framework independent.

---

# 5. Theme Layer

The Theme Layer maps Foundation Tokens into visual themes.

Examples:

- Light Theme
- Dark Theme
- High Contrast Theme
- Future Brand Themes

Themes never modify components directly.

They redefine token mappings.

---

# 6. Semantic Layer

Semantic Tokens translate visual meaning into reusable values.

Examples include:

- Primary colors
- Surface colors
- Success colors
- Border colors
- Text colors

Components consume Semantic Tokens instead of Primitive Tokens.

---

# 7. Utilities

Utilities provide reusable styling helpers.

Examples:

- Display
- Flexbox
- Grid
- Spacing helpers
- Visibility
- Overflow
- Positioning

Utilities must remain generic.

Business-specific utilities are prohibited.

---

# 8. Base Components

Base Components are the smallest reusable UI building blocks.

Examples:

- Button
- Input
- Label
- Checkbox
- Radio
- Badge
- Card
- Avatar

Each component owns its internal implementation while respecting the Design System.

---

# 9. Composite Components

Composite Components combine multiple Base Components into reusable UI patterns.

Examples:

- Product Card
- Navigation Bar
- Search Box
- Shopping Cart Summary
- User Menu
- Pagination
- Data Table

Composite Components must not duplicate logic already provided by Base Components.

---

# 10. Layout Layer

Layouts define page structure.

Responsibilities include:

- Grid systems
- Content containers
- Responsive layouts
- Sidebar organization
- Header positioning
- Footer placement

Layouts never contain business logic.

---

# 11. Page Layer

Pages assemble layouts and components into complete application screens.

Examples:

- Home
- Product Details
- Checkout
- Dashboard
- User Profile

Pages should contain minimal styling.

Most visual decisions belong to lower layers.

---

# 12. Dependency Rules

The following dependency flow is mandatory.

```
Pages
    ↓

Layouts
    ↓

Composite Components
    ↓

Base Components
    ↓

Utilities
    ↓

Semantic Layer
    ↓

Theme Layer
    ↓

Foundation Layer
```

Dependencies must never flow in the opposite direction.

---

# 13. Forbidden Practices

The following practices are prohibited.

- Hardcoded colors
- Hardcoded spacing
- Hardcoded typography
- Hardcoded z-index values
- Hardcoded animation durations
- Primitive Token consumption inside components
- Inline styling without justification
- Duplicate component implementations
- Cross-layer dependencies

---

# 14. Benefits

This architecture provides:

- Predictable development
- High maintainability
- Consistent UI
- Easier testing
- Better scalability
- Theme support
- Reduced technical debt
- Improved onboarding

---

# 15. Future Evolution

Future improvements include:

- Container Query architecture
- CSS Cascade Layers
- Design Token automation
- Theme generation
- Storybook integration
- Visual regression testing
- Figma synchronization

The overall architecture should remain unchanged.

---

# 16. Related Documents

- README.md
- 01-overview.md
- 03-design-principles.md
- 04-token-architecture.md
- 05-roadmap.md
