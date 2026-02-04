# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Pet e-commerce backend built with Django 6.0 and Django REST Framework. Currently in early development with basic scaffolding in place.

## Commands

```bash
# Install dependencies
uv sync

# Add a new dependency
uv add <package>

# Start PostgreSQL database
docker compose up -d

# Run development server
uv run python manage.py runserver

# Run migrations
uv run python manage.py migrate

# Create new migrations after model changes
uv run python manage.py makemigrations

# Run tests
uv run python manage.py test

# Run a single test
uv run python manage.py test api.tests.TestClassName.test_method_name

# Create superuser for admin
uv run python manage.py createsuperuser
```

## Architecture

- **the_project/**: Django project configuration (settings, root urls, wsgi/asgi)
- **api/**: Main application for REST API
  - Uses DRF's `DefaultRouter` for automatic URL routing
  - ViewSets should be registered in `api/urls.py`
  - Models, serializers, and views are empty scaffolds awaiting implementation

## Database

PostgreSQL via Docker Compose on port 5433 (maps to container's 5432). Connection configured via environment variables in `.env` with fallback defaults in settings.

## DRF Configuration

- Default permission: `AllowAny`
- Pagination: `PageNumberPagination` with page size 10
