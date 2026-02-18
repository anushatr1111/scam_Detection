from fastapi import FastAPI
from app.api.router import api_router
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_middleware(LoggingMiddleware)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Welcome to ScamSense AI"}
from app.db.database import Base, engine
from app.models import user

Base.metadata.create_all(bind=engine)
