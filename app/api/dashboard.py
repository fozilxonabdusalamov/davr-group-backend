from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.models import ContactSubmission, QuoteRequest, Service, FleetVehicle, Testimonial
from app.schemas.schemas import DashboardStats

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/stats", response_model=DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return DashboardStats(
        total_contacts=db.query(ContactSubmission).count(),
        unread_contacts=db.query(ContactSubmission).filter(ContactSubmission.is_read == False).count(),
        total_quotes=db.query(QuoteRequest).count(),
        unread_quotes=db.query(QuoteRequest).filter(QuoteRequest.is_read == False).count(),
        total_services=db.query(Service).count(),
        total_vehicles=db.query(FleetVehicle).count(),
        total_testimonials=db.query(Testimonial).count(),
    )
