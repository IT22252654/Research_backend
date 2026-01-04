from fastapi import FastAPI
from app.routes import mood_routes

app = FastAPI(title="Children Mental Health API", version="1.0.0")

# Include route folder
app.include_router(mood_routes.router)
