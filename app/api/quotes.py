from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.models import QuoteRequest
from app.schemas.schemas import QuoteRequestCreate, QuoteRequestUpdate, QuoteRequestOut

router = APIRouter(prefix="/api/quotes", tags=["quotes"])


@router.post("/", response_model=QuoteRequestOut)
def create_quote(data: QuoteRequestCreate, db: Session = Depends(get_db)):
    quote = QuoteRequest(**data.model_dump())
    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote


@router.get("/", response_model=list[QuoteRequestOut])
def get_quotes(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(QuoteRequest).order_by(QuoteRequest.created_at.desc()).all()


@router.put("/{quote_id}", response_model=QuoteRequestOut)
def update_quote(quote_id: int, data: QuoteRequestUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    quote = db.query(QuoteRequest).filter(QuoteRequest.id == quote_id).first()
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(quote, key, value)
    db.commit()
    db.refresh(quote)
    return quote


@router.delete("/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    quote = db.query(QuoteRequest).filter(QuoteRequest.id == quote_id).first()
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    db.delete(quote)
    db.commit()
    return {"detail": "Quote deleted"}
