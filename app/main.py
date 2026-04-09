import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.core.database import engine, Base
from app.api import auth, services, fleet, testimonials, content, contacts, quotes, upload, dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, docs_url="/api/docs", redoc_url="/api/redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(services.router)
app.include_router(fleet.router)
app.include_router(testimonials.router)
app.include_router(content.router)
app.include_router(contacts.router)
app.include_router(quotes.router)
app.include_router(upload.router)
app.include_router(dashboard.router)

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)


@app.get("/api/health")
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}
