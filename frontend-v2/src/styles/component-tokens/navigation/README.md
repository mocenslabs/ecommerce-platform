# Navigation Component Tokens

## Overview

Defines the visual contract for navigation-related components.

Navigation components help users move between pages, sections and application views.

Unlike Disclosure components, navigation changes location rather than revealing hidden content.

---

# Components

- Navbar
- Sidebar
- Breadcrumb
- Pagination

---

# Rules

Each file:

- defines only CSS variables
- contains no CSS classes
- contains no layouts
- contains no component implementation

---

# Dependency Flow

Foundation Tokens

↓

Semantic Tokens

↓

Navigation Component Tokens

↓

Vue Components

---

# Responsibilities

Navigation components define:

- spacing
- colors
- typography
- borders
- elevation
- motion

Behavior, routing and accessibility belong to the Vue components.

---

# Naming Convention

--navbar-*

--sidebar-*

--breadcrumb-*

--pagination-*

---

# Maintenance Notes

Navigation components should reuse Foundation Tokens whenever possible.

Avoid introducing duplicated spacing, colors or typography.
