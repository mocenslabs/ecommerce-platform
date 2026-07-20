# Styles

## Overview

The `styles` directory contains the complete CSS architecture of the Premium E-commerce Platform.

The architecture is based on layered responsibilities to ensure scalability, maintainability and consistency across the entire application.

Each layer has a single responsibility and depends only on lower layers.

---

# Architecture

```
Design Tokens
        │
        ▼
Base Styles
        │
        ▼
Themes
        │
        ▼
Utilities
        │
        ▼
Helpers
        │
        ▼
Components
```

---

# Directory Structure

```
styles/

├── tokens/
├── base/
├── themes/
├── utilities/
├── helpers/

├── index.css
└── README.md
```

---

# Layers

## Tokens

Foundation layer.

Defines reusable design decisions.

Examples:

- Colors
- Typography
- Spacing
- Radius
- Elevation
- Motion
- Breakpoints
- Z-index

Components must never define these values directly.

---

## Base

Provides browser normalization and default HTML styling.

Includes:

- reset.css
- accessibility.css
- typography.css
- forms.css
- media.css

Base styles should never contain business logic.

---

## Themes

Maps Semantic Tokens to Design Tokens.

Themes define the visual identity of the application without changing component implementations.

Examples:

- light.css
- dark.css

---

## Utilities

Reusable CSS helper classes.

Utilities expose generic CSS behaviors.

Examples:

- Display
- Flexbox
- Grid
- Spacing
- Position
- Overflow

Utilities must remain generic and reusable.

---

## Helpers

Reusable animation resources.

Includes:

- Keyframes
- Animation classes

Helpers are consumed by components but never contain component-specific behavior.

---

# Dependency Rules

The dependency flow is strictly one-directional.

```
Tokens
    ↓

Base
    ↓

Themes
    ↓

Utilities
    ↓

Helpers
    ↓

Components
```

Upper layers may consume lower layers.

Lower layers must never depend on upper layers.

---

# Design Principles

The architecture follows these principles:

- Single Responsibility
- Separation of Concerns
- Design Token driven
- Mobile First
- Accessibility First
- Scalable Architecture
- Maintainable CSS
- Predictable Styling

---

# Naming Convention

The project follows a consistent naming strategy.

Examples:

```
color-primary

space-4

font-size-base

duration-normal

transition-fast
```

CSS classes use kebab-case.

```
product-card

animate-fade-in

flex-column

text-center
```

---

# Forbidden Practices

The following practices are prohibited:

- Hardcoded colors
- Hardcoded spacing
- Hardcoded typography
- Hardcoded border radius
- Hardcoded shadows
- Hardcoded animation timing
- Component-specific utilities
- Duplicated Design Tokens

---

# Future Layers

The next architectural layer after `styles` is:

```
Component Tokens
        ↓
Component Library
        ↓
Layouts
        ↓
Views
        ↓
Pages
```

This separation allows components to remain independent from the foundation layer while maintaining consistency across the application.

---

# Maintenance Notes

Before introducing new CSS files:

- Verify the appropriate layer.
- Avoid duplicating existing functionality.
- Reuse Design Tokens whenever possible.
- Prefer composition over duplication.
- Keep responsibilities isolated.
