import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from alembic.config import Config
from alembic import command

from .config.config import get_settings, Settings
from .routers import listing

log = logging.getLogger("uvicorn")


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@asynccontextmanager
async def lifespan(app_: FastAPI):
    log.info("Starting up...")
    log.info("run alembic upgrade head...")
    run_migrations()
    yield
    log.info("Shutting down...")


app = FastAPI(lifespan=lifespan)
app.include_router(listing.router)


@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Welcome to Fourmius.io!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
