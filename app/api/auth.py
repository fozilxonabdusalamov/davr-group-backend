from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import verify_password, create_access_token, get_current_admin
from app.models.models import Admin
from app.schemas.schemas import LoginRequest, Token, AdminOut

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.username == data.username).first()
    if not admin or not verify_password(data.password, admin.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(data={"sub": admin.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=AdminOut)
def get_me(admin: Admin = Depends(get_current_admin)):
    return admin
