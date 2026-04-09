import os
import uuid

from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import FileResponse

from app.core.config import settings
from app.core.security import get_current_admin

router = APIRouter(prefix="/api/upload", tags=["upload"])

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}


@router.post("/")
async def upload_file(file: UploadFile = File(...), admin=Depends(get_current_admin)):
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return {"error": "File type not allowed"}
    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(settings.UPLOAD_DIR, filename)
    content = await file.read()
    with open(filepath, "wb") as f:
        f.write(content)
    return {"filename": filename, "url": f"/api/upload/files/{filename}"}


@router.get("/files/{filename}")
async def get_file(filename: str):
    filepath = os.path.join(settings.UPLOAD_DIR, filename)
    if not os.path.exists(filepath):
        return {"error": "File not found"}
    return FileResponse(filepath)
