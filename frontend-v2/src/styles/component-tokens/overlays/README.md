# Overlay Component Tokens

## Overview

Defines the visual contract for floating surface components.

Overlay components temporarily appear above the normal document flow to display additional content, actions or contextual information.

Unlike persistent surfaces, overlays require elevation management, layering and focus handling.

---

# Components

- Modal
- Drawer
- Dropdown
- Popover
- Tooltip

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

Overlay Component Tokens

↓

Vue Components

---

# Responsibilities

Overlay components define:

- elevation
- background
- borders
- spacing
- radius
- transitions

Overlay positioning and accessibility behavior belong to the Vue components.

---

# Naming Convention

--modal-*

--drawer-*

--dropdown-*

--popover-*

--tooltip-*

---

# Maintenance Notes

Overlay components should consume Foundation Tokens whenever possible.

Avoid duplicating elevation, spacing or radius values.

Behavior such as focus trapping, escape key handling and portal rendering belongs exclusively to the component implementation.
