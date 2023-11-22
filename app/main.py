from fastapi import FastAPI, Depends

from .config.config import get_settings, Settings
from .routers import listing

app = FastAPI()

app.include_router(listing.router)


@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Welcome to Fourmius.io!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
