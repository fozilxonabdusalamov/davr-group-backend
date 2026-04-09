from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.models import ContactSubmission
from app.schemas.schemas import ContactSubmissionCreate, ContactSubmissionOut

router = APIRouter(prefix="/api/contacts", tags=["contacts"])


@router.post("/", response_model=ContactSubmissionOut)
def create_contact(data: ContactSubmissionCreate, db: Session = Depends(get_db)):
    contact = ContactSubmission(**data.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


@router.get("/", response_model=list[ContactSubmissionOut])
def get_contacts(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(ContactSubmission).order_by(ContactSubmission.created_at.desc()).all()


@router.put("/{contact_id}/read")
def mark_contact_read(contact_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    contact = db.query(ContactSubmission).filter(ContactSubmission.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    contact.is_read = True
    db.commit()
    return {"detail": "Marked as read"}


@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    contact = db.query(ContactSubmission).filter(ContactSubmission.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return {"detail": "Contact deleted"}
