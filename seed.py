"""Seed the database with initial data matching the original static frontend."""
import json
from app.core.database import SessionLocal, engine, Base
from app.core.security import hash_password
from app.models.models import (
    Admin, Service, FleetVehicle, FleetFeature, Testimonial,
    Stat, CompanyInfo, TimelineEvent, CompanyValue, WhyChooseUs, HeroSection,
)

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Clear existing data
for model in [Admin, Service, FleetVehicle, FleetFeature, Testimonial,
              Stat, CompanyInfo, TimelineEvent, CompanyValue, WhyChooseUs, HeroSection]:
    db.query(model).delete()
db.commit()

# ---- Admin ----
db.add(Admin(username="admin", password_hash=hash_password("admin123"), full_name="Admin"))
db.commit()

# ---- Hero Section ----
db.add(HeroSection(
    title="Reliable Trucking Services Across the USA",
    subtitle="Davr Group LLC provides professional freight transportation services across all 48 contiguous states. Fast, safe, and on-time delivery you can count on.",
    button_text="Get a Free Quote",
    button_link="/quote",
    is_active=True,
    order=0,
))
db.commit()

# ---- Services ----
services_data = [
    {
        "title": "Full Truckload (FTL)",
        "description": "Dedicated truck for your full-size shipments. Direct door-to-door delivery across all 48 states with no stops, no delays.",
        "icon": "Truck",
        "features": json.dumps(["Direct door-to-door delivery", "Dedicated trailer", "Faster transit times", "Ideal for 10,000+ lbs"]),
        "is_featured": True,
        "order": 0,
    },
    {
        "title": "Less Than Truckload (LTL)",
        "description": "Cost-effective solution for smaller freight. Share trailer space and save on shipping costs without sacrificing quality.",
        "icon": "Package",
        "features": json.dumps(["Cost-effective for smaller loads", "Shared trailer space", "Flexible scheduling", "Great for 100-10,000 lbs"]),
        "is_featured": True,
        "order": 1,
    },
    {
        "title": "Interstate Freight Transportation",
        "description": "Professional point-to-point freight transportation across state lines. Experienced route planning with full regulatory compliance.",
        "icon": "Route",
        "features": json.dumps(["48-state coverage", "Experienced route planning", "Regulatory compliance", "Cross-country capability"]),
        "is_featured": True,
        "order": 2,
    },
    {
        "title": "Expedited Shipping",
        "description": "Time-sensitive deliveries handled with priority. When deadlines matter, count on our expedited freight services.",
        "icon": "Zap",
        "features": json.dumps(["Priority handling", "Optimized routing", "Real-time updates", "Dedicated communication"]),
        "is_featured": True,
        "order": 3,
    },
    {
        "title": "General Freight Delivery",
        "description": "Reliable general freight transportation for all your standard shipping needs. Professional handling of dry van cargo and palletized goods.",
        "icon": "Box",
        "features": json.dumps(["Dry van cargo", "Palletized goods", "Professional handling", "Reliable scheduling"]),
        "is_featured": False,
        "order": 4,
    },
]
for s in services_data:
    db.add(Service(**s))
db.commit()

# ---- Stats ----
stats_data = [
    {"label": "Active Trucks", "value": "3", "icon": "Truck", "suffix": "", "order": 0},
    {"label": "Pro Drivers", "value": "5", "icon": "Users", "suffix": "", "order": 1},
    {"label": "States Covered", "value": "48", "icon": "MapPin", "suffix": "", "order": 2},
    {"label": "On-Time Rate", "value": "98", "icon": "Clock", "suffix": "%", "order": 3},
]
for s in stats_data:
    db.add(Stat(**s))
db.commit()

# ---- Fleet Vehicles ----
vehicles_data = [
    {"unit_number": "Unit #101", "vehicle_type": "Dry Van 53' Trailer", "capacity": "45,000 lbs", "year": 2023, "features": json.dumps(["GPS Enabled", "DOT Compliant", "ELD Equipped", "Dash Cam"]), "status": "Active", "order": 0},
    {"unit_number": "Unit #102", "vehicle_type": "Dry Van 53' Trailer", "capacity": "44,000 lbs", "year": 2022, "features": json.dumps(["GPS Enabled", "DOT Compliant", "ELD Equipped", "Dash Cam"]), "status": "Active", "order": 1},
    {"unit_number": "Unit #103", "vehicle_type": "Dry Van 53' Trailer", "capacity": "45,000 lbs", "year": 2024, "features": json.dumps(["GPS Enabled", "DOT Compliant", "ELD Equipped", "Dash Cam"]), "status": "Active", "order": 2},
]
for v in vehicles_data:
    db.add(FleetVehicle(**v))
db.commit()

# ---- Fleet Features ----
fleet_features_data = [
    {"title": "Regular Maintenance", "description": "All vehicles undergo scheduled preventive maintenance", "icon": "Wrench", "order": 0},
    {"title": "GPS Tracking", "description": "Real-time location tracking on all vehicles", "icon": "MapPin", "order": 1},
    {"title": "Nationwide Coverage", "description": "Operating across all 48 contiguous states", "icon": "Globe", "order": 2},
    {"title": "Safety Compliant", "description": "Full DOT compliance and safety standards", "icon": "Shield", "order": 3},
    {"title": "Modern Equipment", "description": "Late-model trucks with latest technology", "icon": "Cpu", "order": 4},
    {"title": "Dedicated Fleet", "description": "Well-maintained dedicated fleet of trucks", "icon": "Truck", "order": 5},
]
for f in fleet_features_data:
    db.add(FleetFeature(**f))
db.commit()

# ---- Testimonials ----
testimonials_data = [
    {"name": "Michael Chen", "company": "Pacific Logistics", "role": "Logistics Manager", "content": "Davr Group has been our go-to carrier for the past year. Their reliability and communication are outstanding. Every load is delivered on time.", "rating": 5, "order": 0},
    {"name": "Sarah Williams", "company": "Midwest Distributors", "role": "Operations Director", "content": "Working with Davr Group has streamlined our shipping operations. Their drivers are professional and their tracking system keeps us informed.", "rating": 5, "order": 1},
    {"name": "James Rodriguez", "company": "Atlantic Supply Co.", "role": "Supply Chain Manager", "content": "The team at Davr Group goes above and beyond. They've handled our expedited shipments flawlessly. Highly recommended for any freight needs.", "rating": 5, "order": 2},
]
for t in testimonials_data:
    db.add(Testimonial(**t))
db.commit()

# ---- Why Choose Us ----
why_data = [
    {"title": "On-Time Delivery", "description": "We pride ourselves on consistent, punctual deliveries across all routes", "icon": "Clock", "stat_value": "98%", "stat_label": "On-Time Rate", "order": 0},
    {"title": "Experienced Drivers", "description": "Our team of professional drivers brings years of safe driving experience", "icon": "Users", "stat_value": "5+", "stat_label": "Years Avg Experience", "order": 1},
    {"title": "Safe Transportation", "description": "Zero incidents record with full DOT compliance and safety protocols", "icon": "Shield", "stat_value": "0", "stat_label": "Safety Incidents", "order": 2},
    {"title": "24/7 Support", "description": "Round-the-clock dispatch and customer support for all your needs", "icon": "Headphones", "stat_value": "24/7", "stat_label": "Available Support", "order": 3},
]
for w in why_data:
    db.add(WhyChooseUs(**w))
db.commit()

# ---- Company Values ----
values_data = [
    {"title": "Safety First", "description": "Safety is our top priority in everything we do, from driver training to vehicle maintenance.", "icon": "Shield", "order": 0},
    {"title": "Reliability", "description": "We deliver on our promises. When we say on-time, we mean it.", "icon": "Clock", "order": 1},
    {"title": "Transparency", "description": "Real-time tracking and open communication keep you informed every step of the way.", "icon": "Eye", "order": 2},
    {"title": "Partnership", "description": "We treat every client relationship as a long-term partnership built on trust.", "icon": "Handshake", "order": 3},
]
for v in values_data:
    db.add(CompanyValue(**v))
db.commit()

# ---- Timeline ----
timeline_data = [
    {"title": "Company Founded", "description": "Davr Group LLC was established in Saint Louis, Missouri with a vision to provide reliable freight transportation.", "year": "2022", "icon": "Flag", "order": 0},
    {"title": "Fleet Expansion", "description": "Expanded our fleet to 3 trucks and grew our team of professional drivers.", "year": "2023", "icon": "TrendingUp", "order": 1},
    {"title": "Trusted Partner", "description": "Established ourselves as a trusted carrier across all 48 contiguous states.", "year": "2024", "icon": "Award", "order": 2},
]
for t in timeline_data:
    db.add(TimelineEvent(**t))
db.commit()

# ---- Company Info ----
info_data = [
    {"key": "phone", "value": "(314) 555-0123", "category": "contact"},
    {"key": "email", "value": "info@davrgroup.com", "category": "contact"},
    {"key": "address", "value": "Saint Louis, Missouri, USA", "category": "contact"},
    {"key": "hours", "value": "Mon-Fri 7 AM - 7 PM CST", "category": "contact"},
    {"key": "emergency", "value": "24/7 Emergency Dispatch Available", "category": "contact"},
    {"key": "about_title", "value": "Our Story", "category": "about"},
    {"key": "about_description", "value": "Founded in Saint Louis, Missouri, Davr Group LLC started with a simple mission: to provide reliable, safe, and efficient freight transportation across the United States. What began as a small operation has grown into a trusted carrier serving all 48 contiguous states.", "category": "about"},
    {"key": "about_mission", "value": "Our mission is to be the most reliable trucking partner for businesses across America, delivering every load safely, on time, and with complete transparency.", "category": "about"},
    {"key": "company_name", "value": "Davr Group LLC", "category": "general"},
    {"key": "tagline", "value": "Small Company With Big Reliability", "category": "general"},
    {"key": "map_embed", "value": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d398513.4504891!2d-90.70280685!3d38.62774335!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87d8b4a9faed8ef9%3A0xbe39eaca22bbe509!2sSt.%20Louis%2C%20MO!5e0!3m2!1sen!2sus!4v1234567890", "category": "contact"},
]
for i in info_data:
    db.add(CompanyInfo(**i))
db.commit()

db.close()
print("Database seeded successfully!")
print("Admin credentials: username=admin, password=admin123")
