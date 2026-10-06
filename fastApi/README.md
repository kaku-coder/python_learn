# FastAPI Project Structure

This project can be organized by responsibility so that routes, database code,
validation schemas, and business logic stay separate as the app grows.

```text
fastApi/
├── main.py
├── database/
│   ├── __init__.py
│   └── connection.py
├── models/
│   ├── __init__.py
│   └── user.py
├── schemas/
│   ├── __init__.py
│   └── user.py
├── routes/
│   ├── __init__.py
│   └── form_validraton.py
└── services/
    ├── __init__.py
    └── user_service.py
```

## What each part does

- `main.py`: creates the FastAPI app and connects the routers.
- `routes/`: defines API endpoints, such as `GET /users` or `POST /users`.
- `schemas/`: defines Pydantic request and response shapes.
- `models/`: defines database models (when a database is added).
- `database/connection.py`: creates and provides the database connection.
- `services/`: contains application logic used by routes.
- `__init__.py`: marks a folder as a Python package.

## Connect the user routes to the app

The route file currently in this project is `routes/form_validraton.py`. It
defines an `APIRouter` and a `POST /users` endpoint. In `main.py`, import and
include that router after creating the app:

```python
from fastapi import FastAPI
from routes.form_validraton import router as user_router

app = FastAPI()
app.include_router(user_router, prefix="/api", tags=["Users"])
```

The endpoint will then be available at `POST /api/users`. The `prefix` is
optional; without it, the endpoint path will be `POST /users`.

## Run the app

From the project folder, run:

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to try the API in FastAPI's interactive docs.
