# Developer Onboarding Guide

## Purpose

This guide helps new contributors set up the development environment and start contributing to the project as quickly as possible.

---

# Prerequisites

Required software:

- Git
- Python 3.12
- Node.js LTS
- Docker
- Docker Compose

Recommended tools:

- Visual Studio Code
- PyCharm Professional or Community
- Postman or Bruno
- GitHub CLI

---

# Repository Structure

```text
backend/
frontend/
docs/
scripts/
.github/
```

---

# Clone the Repository

```bash
git clone https://github.com/<organization>/<repository>.git

cd <repository>
```

---

# Backend Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment variables:

```text
.env
```

Run migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

---

# Frontend Setup

(Will be completed once the frontend is implemented.)

---

# Docker Setup

```bash
docker compose up --build
```

---

# Running Tests

```bash
pytest
```

Coverage:

```bash
coverage run -m pytest
coverage html
```

---

# Code Quality

Before creating a Pull Request, execute:

```bash
ruff check .
black .
isort .
pytest
```

---

# Documentation

Every new feature should update:

- API Reference
- Business Rules (if applicable)
- README (if applicable)

---

# Pull Request Checklist

- Tests passing
- Documentation updated
- Code formatted
- No secrets committed
- CI passing

---

# Getting Help

Review:

- Backend Handbook
- ADRs
- API Reference

before opening a discussion.
