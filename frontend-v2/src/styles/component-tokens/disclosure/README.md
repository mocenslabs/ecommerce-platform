# Disclosure Component Tokens

## Overview

Defines the visual contract for disclosure-related components.

Disclosure components progressively reveal or organize content without changing the current navigation context.

Unlike Navigation components, disclosure components manage visibility within the current view.

---

# Components

- Accordion
- Tabs

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

Disclosure Component Tokens

↓

Vue Components

---

# Responsibilities

Disclosure components define:

- spacing
- typography
- borders
- colors
- motion

State management and accessibility belong to the Vue implementation.

---

# Naming Convention

--accordion-*

--tabs-*

---

# Maintenance Notes

Disclosure components should remain lightweight and reuse Foundation Tokens whenever possible.

Avoid introducing duplicated spacing, typography or color values.
