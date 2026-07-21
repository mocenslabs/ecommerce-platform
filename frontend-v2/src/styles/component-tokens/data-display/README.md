# Data Display Component Tokens

## Overview

Defines the visual contract for components responsible for presenting data.

Data Display components organize, summarize and present information without collecting user input.

---

# Components

- Avatar
- Table

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

Data Display Component Tokens

↓

Vue Components

---

# Responsibilities

Data Display components define:

- typography
- spacing
- borders
- colors
- elevation
- motion

Sorting, filtering, pagination and interactions belong to the Vue implementation.

---

# Naming Convention

--avatar-*

--table-*

---

# Maintenance Notes

Data Display components should prioritize readability and consistency.

Avoid introducing duplicated typography, spacing or border values.
