from fastapi import FastAPI
from app.api import health

app = FastAPI(title="banter", version="0.1.0", description="A simple chat application")

app.include_router(health.router)

