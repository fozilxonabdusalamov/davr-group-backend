from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.models import (
    Stat, CompanyInfo, TimelineEvent, CompanyValue, WhyChooseUs, HeroSection,
)
from app.schemas.schemas import (
    StatCreate, StatUpdate, StatOut,
    CompanyInfoCreate, CompanyInfoUpdate, CompanyInfoOut,
    TimelineEventCreate, TimelineEventUpdate, TimelineEventOut,
    CompanyValueCreate, CompanyValueUpdate, CompanyValueOut,
    WhyChooseUsCreate, WhyChooseUsUpdate, WhyChooseUsOut,
    HeroSectionCreate, HeroSectionUpdate, HeroSectionOut,
)

router = APIRouter(prefix="/api/content", tags=["content"])


# ---- Stats ----
@router.get("/stats", response_model=list[StatOut])
def get_stats(db: Session = Depends(get_db)):
    return db.query(Stat).order_by(Stat.order).all()


@router.post("/stats", response_model=StatOut)
def create_stat(data: StatCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    stat = Stat(**data.model_dump())
    db.add(stat)
    db.commit()
    db.refresh(stat)
    return stat


@router.put("/stats/{stat_id}", response_model=StatOut)
def update_stat(stat_id: int, data: StatUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    stat = db.query(Stat).filter(Stat.id == stat_id).first()
    if not stat:
        raise HTTPException(status_code=404, detail="Stat not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(stat, key, value)
    db.commit()
    db.refresh(stat)
    return stat


@router.delete("/stats/{stat_id}")
def delete_stat(stat_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    stat = db.query(Stat).filter(Stat.id == stat_id).first()
    if not stat:
        raise HTTPException(status_code=404, detail="Stat not found")
    db.delete(stat)
    db.commit()
    return {"detail": "Stat deleted"}


# ---- Company Info ----
@router.get("/company-info", response_model=list[CompanyInfoOut])
def get_company_info(db: Session = Depends(get_db)):
    return db.query(CompanyInfo).all()


@router.get("/company-info/{key}", response_model=CompanyInfoOut)
def get_company_info_by_key(key: str, db: Session = Depends(get_db)):
    info = db.query(CompanyInfo).filter(CompanyInfo.key == key).first()
    if not info:
        raise HTTPException(status_code=404, detail="Company info not found")
    return info


@router.post("/company-info", response_model=CompanyInfoOut)
def create_company_info(data: CompanyInfoCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    existing = db.query(CompanyInfo).filter(CompanyInfo.key == data.key).first()
    if existing:
        existing.value = data.value
        existing.category = data.category
        db.commit()
        db.refresh(existing)
        return existing
    info = CompanyInfo(**data.model_dump())
    db.add(info)
    db.commit()
    db.refresh(info)
    return info


@router.put("/company-info/{info_id}", response_model=CompanyInfoOut)
def update_company_info(info_id: int, data: CompanyInfoUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    info = db.query(CompanyInfo).filter(CompanyInfo.id == info_id).first()
    if not info:
        raise HTTPException(status_code=404, detail="Company info not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(info, key, value)
    db.commit()
    db.refresh(info)
    return info


@router.delete("/company-info/{info_id}")
def delete_company_info(info_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    info = db.query(CompanyInfo).filter(CompanyInfo.id == info_id).first()
    if not info:
        raise HTTPException(status_code=404, detail="Company info not found")
    db.delete(info)
    db.commit()
    return {"detail": "Company info deleted"}


# ---- Timeline Events ----
@router.get("/timeline", response_model=list[TimelineEventOut])
def get_timeline(db: Session = Depends(get_db)):
    return db.query(TimelineEvent).order_by(TimelineEvent.order).all()


@router.post("/timeline", response_model=TimelineEventOut)
def create_timeline_event(data: TimelineEventCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    event = TimelineEvent(**data.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.put("/timeline/{event_id}", response_model=TimelineEventOut)
def update_timeline_event(event_id: int, data: TimelineEventUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    event = db.query(TimelineEvent).filter(TimelineEvent.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Timeline event not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(event, key, value)
    db.commit()
    db.refresh(event)
    return event


@router.delete("/timeline/{event_id}")
def delete_timeline_event(event_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    event = db.query(TimelineEvent).filter(TimelineEvent.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Timeline event not found")
    db.delete(event)
    db.commit()
    return {"detail": "Timeline event deleted"}


# ---- Company Values ----
@router.get("/values", response_model=list[CompanyValueOut])
def get_values(db: Session = Depends(get_db)):
    return db.query(CompanyValue).order_by(CompanyValue.order).all()


@router.post("/values", response_model=CompanyValueOut)
def create_value(data: CompanyValueCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    value = CompanyValue(**data.model_dump())
    db.add(value)
    db.commit()
    db.refresh(value)
    return value


@router.put("/values/{value_id}", response_model=CompanyValueOut)
def update_value(value_id: int, data: CompanyValueUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    value = db.query(CompanyValue).filter(CompanyValue.id == value_id).first()
    if not value:
        raise HTTPException(status_code=404, detail="Company value not found")
    for key, val in data.model_dump(exclude_unset=True).items():
        setattr(value, key, val)
    db.commit()
    db.refresh(value)
    return value


@router.delete("/values/{value_id}")
def delete_value(value_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    value = db.query(CompanyValue).filter(CompanyValue.id == value_id).first()
    if not value:
        raise HTTPException(status_code=404, detail="Company value not found")
    db.delete(value)
    db.commit()
    return {"detail": "Company value deleted"}


# ---- Why Choose Us ----
@router.get("/why-choose-us", response_model=list[WhyChooseUsOut])
def get_why_choose_us(db: Session = Depends(get_db)):
    return db.query(WhyChooseUs).order_by(WhyChooseUs.order).all()


@router.post("/why-choose-us", response_model=WhyChooseUsOut)
def create_why_choose_us(data: WhyChooseUsCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    item = WhyChooseUs(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/why-choose-us/{item_id}", response_model=WhyChooseUsOut)
def update_why_choose_us(item_id: int, data: WhyChooseUsUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    item = db.query(WhyChooseUs).filter(WhyChooseUs.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/why-choose-us/{item_id}")
def delete_why_choose_us(item_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    item = db.query(WhyChooseUs).filter(WhyChooseUs.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted"}


# ---- Hero Section ----
@router.get("/hero", response_model=list[HeroSectionOut])
def get_hero_sections(db: Session = Depends(get_db)):
    return db.query(HeroSection).filter(HeroSection.is_active == True).order_by(HeroSection.order).all()


@router.get("/hero/all", response_model=list[HeroSectionOut])
def get_all_hero_sections(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(HeroSection).order_by(HeroSection.order).all()


@router.post("/hero", response_model=HeroSectionOut)
def create_hero_section(data: HeroSectionCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    hero = HeroSection(**data.model_dump())
    db.add(hero)
    db.commit()
    db.refresh(hero)
    return hero


@router.put("/hero/{hero_id}", response_model=HeroSectionOut)
def update_hero_section(hero_id: int, data: HeroSectionUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    hero = db.query(HeroSection).filter(HeroSection.id == hero_id).first()
    if not hero:
        raise HTTPException(status_code=404, detail="Hero section not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(hero, key, value)
    db.commit()
    db.refresh(hero)
    return hero


@router.delete("/hero/{hero_id}")
def delete_hero_section(hero_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    hero = db.query(HeroSection).filter(HeroSection.id == hero_id).first()
    if not hero:
        raise HTTPException(status_code=404, detail="Hero section not found")
    db.delete(hero)
    db.commit()
    return {"detail": "Hero section deleted"}
