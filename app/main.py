from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()


@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Welcome to Fourmius.io!",
        "environment": settings.environment,
        "testing": settings.testing
    }
