from pydantic import BaseModel, EmailStr
from datetime import datetime


# ---- Auth ----
class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AdminOut(BaseModel):
    id: int
    username: str
    full_name: str

    class Config:
        from_attributes = True


# ---- Service ----
class ServiceBase(BaseModel):
    title: str
    description: str
    icon: str = "Truck"
    features: str = "[]"
    image: str = ""
    is_featured: bool = False
    order: int = 0


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    icon: str | None = None
    features: str | None = None
    image: str | None = None
    is_featured: bool | None = None
    order: int | None = None


class ServiceOut(ServiceBase):
    id: int
    created_at: datetime | None = None

    class Config:
        from_attributes = True


# ---- Fleet Vehicle ----
class FleetVehicleBase(BaseModel):
    unit_number: str
    vehicle_type: str = "Dry Van 53' Trailer"
    capacity: str = "44,000 lbs"
    year: int = 2024
    features: str = "[]"
    status: str = "Active"
    image: str = ""
    order: int = 0


class FleetVehicleCreate(FleetVehicleBase):
    pass


class FleetVehicleUpdate(BaseModel):
    unit_number: str | None = None
    vehicle_type: str | None = None
    capacity: str | None = None
    year: int | None = None
    features: str | None = None
    status: str | None = None
    image: str | None = None
    order: int | None = None


class FleetVehicleOut(FleetVehicleBase):
    id: int
    created_at: datetime | None = None

    class Config:
        from_attributes = True


# ---- Fleet Feature ----
class FleetFeatureBase(BaseModel):
    title: str
    description: str = ""
    icon: str = "Shield"
    order: int = 0


class FleetFeatureCreate(FleetFeatureBase):
    pass


class FleetFeatureUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    icon: str | None = None
    order: int | None = None


class FleetFeatureOut(FleetFeatureBase):
    id: int

    class Config:
        from_attributes = True


# ---- Testimonial ----
class TestimonialBase(BaseModel):
    name: str
    company: str = ""
    role: str = ""
    content: str
    rating: int = 5
    avatar: str = ""
    is_visible: bool = True
    order: int = 0


class TestimonialCreate(TestimonialBase):
    pass


class TestimonialUpdate(BaseModel):
    name: str | None = None
    company: str | None = None
    role: str | None = None
    content: str | None = None
    rating: int | None = None
    avatar: str | None = None
    is_visible: bool | None = None
    order: int | None = None


class TestimonialOut(TestimonialBase):
    id: int
    created_at: datetime | None = None

    class Config:
        from_attributes = True


# ---- Stat ----
class StatBase(BaseModel):
    label: str
    value: str
    icon: str = ""
    suffix: str = ""
    order: int = 0


class StatCreate(StatBase):
    pass


class StatUpdate(BaseModel):
    label: str | None = None
    value: str | None = None
    icon: str | None = None
    suffix: str | None = None
    order: int | None = None


class StatOut(StatBase):
    id: int

    class Config:
        from_attributes = True


# ---- Company Info ----
class CompanyInfoBase(BaseModel):
    key: str
    value: str
    category: str = "general"


class CompanyInfoCreate(CompanyInfoBase):
    pass


class CompanyInfoUpdate(BaseModel):
    value: str | None = None
    category: str | None = None


class CompanyInfoOut(CompanyInfoBase):
    id: int

    class Config:
        from_attributes = True


# ---- Timeline Event ----
class TimelineEventBase(BaseModel):
    title: str
    description: str = ""
    year: str = ""
    icon: str = ""
    order: int = 0


class TimelineEventCreate(TimelineEventBase):
    pass


class TimelineEventUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    year: str | None = None
    icon: str | None = None
    order: int | None = None


class TimelineEventOut(TimelineEventBase):
    id: int

    class Config:
        from_attributes = True


# ---- Company Value ----
class CompanyValueBase(BaseModel):
    title: str
    description: str = ""
    icon: str = "Shield"
    order: int = 0


class CompanyValueCreate(CompanyValueBase):
    pass


class CompanyValueUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    icon: str | None = None
    order: int | None = None


class CompanyValueOut(CompanyValueBase):
    id: int

    class Config:
        from_attributes = True


# ---- Why Choose Us ----
class WhyChooseUsBase(BaseModel):
    title: str
    description: str = ""
    icon: str = ""
    stat_value: str = ""
    stat_label: str = ""
    order: int = 0


class WhyChooseUsCreate(WhyChooseUsBase):
    pass


class WhyChooseUsUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    icon: str | None = None
    stat_value: str | None = None
    stat_label: str | None = None
    order: int | None = None


class WhyChooseUsOut(WhyChooseUsBase):
    id: int

    class Config:
        from_attributes = True


# ---- Contact Submission ----
class ContactSubmissionCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str = ""
    subject: str = ""
    message: str


class ContactSubmissionOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    subject: str
    message: str
    is_read: bool
    created_at: datetime | None = None

    class Config:
        from_attributes = True


# ---- Quote Request ----
class QuoteRequestCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str = ""
    company: str = ""
    pickup_location: str = ""
    delivery_location: str = ""
    weight: str = ""
    freight_type: str = ""
    service_type: str = ""
    pickup_date: str = ""
    notes: str = ""


class QuoteRequestUpdate(BaseModel):
    status: str | None = None
    is_read: bool | None = None


class QuoteRequestOut(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str
    company: str
    pickup_location: str
    delivery_location: str
    weight: str
    freight_type: str
    service_type: str
    pickup_date: str
    notes: str
    status: str
    is_read: bool
    created_at: datetime | None = None

    class Config:
        from_attributes = True


# ---- Legal Page ----
class LegalSectionItem(BaseModel):
    heading: str = ""
    content: str = ""


class LegalPageBase(BaseModel):
    slug: str
    title: str
    sections: str = "[]"  # JSON string of LegalSectionItem[]
    last_updated: str = ""


class LegalPageCreate(LegalPageBase):
    pass


class LegalPageUpdate(BaseModel):
    title: str | None = None
    sections: str | None = None
    last_updated: str | None = None


class LegalPageOut(LegalPageBase):
    id: int
    updated_at: datetime | None = None

    class Config:
        from_attributes = True


# ---- Hero Section ----
class HeroSectionBase(BaseModel):
    title: str
    subtitle: str = ""
    button_text: str = "Get a Free Quote"
    button_link: str = "/quote"
    background_image: str = ""
    is_active: bool = True
    order: int = 0


class HeroSectionCreate(HeroSectionBase):
    pass


class HeroSectionUpdate(BaseModel):
    title: str | None = None
    subtitle: str | None = None
    button_text: str | None = None
    button_link: str | None = None
    background_image: str | None = None
    is_active: bool | None = None
    order: int | None = None


class HeroSectionOut(HeroSectionBase):
    id: int

    class Config:
        from_attributes = True


# ---- Dashboard Stats ----
class DashboardStats(BaseModel):
    total_contacts: int
    unread_contacts: int
    total_quotes: int
    unread_quotes: int
    total_services: int
    total_vehicles: int
    total_testimonials: int
