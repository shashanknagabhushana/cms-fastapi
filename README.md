# CMS Backend using FastAPI

This project is a small production-style Content Management System (CMS) backend built using FastAPI.

## Features
- CRUD operations for content items
- MongoDB for content storage
- Redis for caching rendered HTML
- Jinja2 templating engine
- Dynamic HTML page rendering
- OpenAPI documentation

## Tech Stack
- FastAPI
- MongoDB
- Redis
- Jinja2
- Python

## How to Run

1. Install dependencies:

2. Start MongoDB and Redis locally

3. Run the server:

4. Open API docs:

## API Endpoints
- POST /content
- GET /content
- PUT /content/{id}
- DELETE /content/{id}
- GET /render/{id}

## Notes
This is a backend-only project. No frontend UI is required.
