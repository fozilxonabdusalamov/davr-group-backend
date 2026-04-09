from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Float
from sqlalchemy.sql import func

from app.core.database import Base


class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(200), default="")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    icon = Column(String(100), default="Truck")
    features = Column(Text, default="")  # JSON string array
    image = Column(String(500), default="")
    is_featured = Column(Boolean, default=False)
    order = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class FleetVehicle(Base):
    __tablename__ = "fleet_vehicles"
    id = Column(Integer, primary_key=True, index=True)
    unit_number = Column(String(50), nullable=False)
    vehicle_type = Column(String(200), default="Dry Van 53' Trailer")
    capacity = Column(String(100), default="44,000 lbs")
    year = Column(Integer, default=2024)
    features = Column(Text, default="")  # JSON string array
    status = Column(String(50), default="Active")
    image = Column(String(500), default="")
    order = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class FleetFeature(Base):
    __tablename__ = "fleet_features"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, default="")
    icon = Column(String(100), default="Shield")
    order = Column(Integer, default=0)


class Testimonial(Base):
    __tablename__ = "testimonials"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    company = Column(String(200), default="")
    role = Column(String(200), default="")
    content = Column(Text, nullable=False)
    rating = Column(Integer, default=5)
    avatar = Column(String(500), default="")
    is_visible = Column(Boolean, default=True)
    order = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Stat(Base):
    __tablename__ = "stats"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(200), nullable=False)
    value = Column(String(100), nullable=False)
    icon = Column(String(100), default="")
    suffix = Column(String(50), default="")
    order = Column(Integer, default=0)


class CompanyInfo(Base):
    __tablename__ = "company_info"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), unique=True, nullable=False)
    value = Column(Text, nullable=False)
    category = Column(String(100), default="general")  # general, contact, social, about


class TimelineEvent(Base):
    __tablename__ = "timeline_events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, default="")
    year = Column(String(20), default="")
    icon = Column(String(100), default="")
    order = Column(Integer, default=0)


class CompanyValue(Base):
    __tablename__ = "company_values"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, default="")
    icon = Column(String(100), default="Shield")
    order = Column(Integer, default=0)


class WhyChooseUs(Base):
    __tablename__ = "why_choose_us"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, default="")
    icon = Column(String(100), default="")
    stat_value = Column(String(50), default="")
    stat_label = Column(String(100), default="")
    order = Column(Integer, default=0)


class ContactSubmission(Base):
    __tablename__ = "contact_submissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    phone = Column(String(50), default="")
    subject = Column(String(300), default="")
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class QuoteRequest(Base):
    __tablename__ = "quote_requests"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    phone = Column(String(50), default="")
    company = Column(String(200), default="")
    pickup_location = Column(String(300), default="")
    delivery_location = Column(String(300), default="")
    weight = Column(String(100), default="")
    freight_type = Column(String(100), default="")
    service_type = Column(String(100), default="")
    pickup_date = Column(String(50), default="")
    notes = Column(Text, default="")
    status = Column(String(50), default="new")  # new, reviewed, quoted, accepted, rejected
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class HeroSection(Base):
    __tablename__ = "hero_sections"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    subtitle = Column(Text, default="")
    button_text = Column(String(100), default="Get a Free Quote")
    button_link = Column(String(200), default="/quote")
    background_image = Column(String(500), default="")
    is_active = Column(Boolean, default=True)
    order = Column(Integer, default=0)
