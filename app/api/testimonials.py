from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.models import Testimonial
from app.schemas.schemas import TestimonialCreate, TestimonialUpdate, TestimonialOut

router = APIRouter(prefix="/api/testimonials", tags=["testimonials"])


@router.get("/", response_model=list[TestimonialOut])
def get_testimonials(db: Session = Depends(get_db)):
    return db.query(Testimonial).filter(Testimonial.is_visible == True).order_by(Testimonial.order).all()


@router.get("/all", response_model=list[TestimonialOut])
def get_all_testimonials(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(Testimonial).order_by(Testimonial.order).all()


@router.post("/", response_model=TestimonialOut)
def create_testimonial(data: TestimonialCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    testimonial = Testimonial(**data.model_dump())
    db.add(testimonial)
    db.commit()
    db.refresh(testimonial)
    return testimonial


@router.put("/{testimonial_id}", response_model=TestimonialOut)
def update_testimonial(testimonial_id: int, data: TestimonialUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    testimonial = db.query(Testimonial).filter(Testimonial.id == testimonial_id).first()
    if not testimonial:
        raise HTTPException(status_code=404, detail="Testimonial not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(testimonial, key, value)
    db.commit()
    db.refresh(testimonial)
    return testimonial


@router.delete("/{testimonial_id}")
def delete_testimonial(testimonial_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    testimonial = db.query(Testimonial).filter(Testimonial.id == testimonial_id).first()
    if not testimonial:
        raise HTTPException(status_code=404, detail="Testimonial not found")
    db.delete(testimonial)
    db.commit()
    return {"detail": "Testimonial deleted"}
