from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Starter",
    description="A FastAPI starter application with authentication functionality",
    version="1.0.0"
)

from app.modules.todo.routers import route as todo_route
from app.modules.auth.routers import route as auth_route


@app.get("/")
def read_root():
    return {
        "name": "FastAPI Starter",
        "version": "1.0.0",
        "description": "A FastAPI starter application with authentication functionality",
        "modules": {
            "auth": "Authentication and user management",
            "todo": "Todo list management"
        },
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }


# Include router
app.include_router(auth_route)
app.include_router(todo_route)

