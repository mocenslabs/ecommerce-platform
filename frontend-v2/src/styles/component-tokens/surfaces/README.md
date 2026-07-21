# Surface Component Tokens

## Overview

Defines the visual contract for persistent surface components.

Surface components provide structure, grouping and visual hierarchy throughout the application.

Unlike overlays, surfaces remain part of the normal document flow.

---

# Components

- Card
- Paper
- Divider

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

Surface Component Tokens

↓

Vue Components

---

# Naming Convention

--card-*

--paper-*

--divider-*

---

# Responsibilities

Surface components define:

- background
- border
- radius
- elevation
- spacing
- motion

They never define layout behavior.

---

# Maintenance Notes

Surface components should consume existing Foundation Tokens whenever possible.

Avoid duplicating spacing, elevation or radius values.
