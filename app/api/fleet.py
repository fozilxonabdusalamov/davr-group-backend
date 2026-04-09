from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.models import FleetVehicle, FleetFeature
from app.schemas.schemas import (
    FleetVehicleCreate, FleetVehicleUpdate, FleetVehicleOut,
    FleetFeatureCreate, FleetFeatureUpdate, FleetFeatureOut,
)

router = APIRouter(prefix="/api/fleet", tags=["fleet"])


# ---- Vehicles ----
@router.get("/vehicles", response_model=list[FleetVehicleOut])
def get_vehicles(db: Session = Depends(get_db)):
    return db.query(FleetVehicle).order_by(FleetVehicle.order).all()


@router.post("/vehicles", response_model=FleetVehicleOut)
def create_vehicle(data: FleetVehicleCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    vehicle = FleetVehicle(**data.model_dump())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle


@router.put("/vehicles/{vehicle_id}", response_model=FleetVehicleOut)
def update_vehicle(vehicle_id: int, data: FleetVehicleUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    vehicle = db.query(FleetVehicle).filter(FleetVehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(vehicle, key, value)
    db.commit()
    db.refresh(vehicle)
    return vehicle


@router.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    vehicle = db.query(FleetVehicle).filter(FleetVehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    db.delete(vehicle)
    db.commit()
    return {"detail": "Vehicle deleted"}


# ---- Features ----
@router.get("/features", response_model=list[FleetFeatureOut])
def get_features(db: Session = Depends(get_db)):
    return db.query(FleetFeature).order_by(FleetFeature.order).all()


@router.post("/features", response_model=FleetFeatureOut)
def create_feature(data: FleetFeatureCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    feature = FleetFeature(**data.model_dump())
    db.add(feature)
    db.commit()
    db.refresh(feature)
    return feature


@router.put("/features/{feature_id}", response_model=FleetFeatureOut)
def update_feature(feature_id: int, data: FleetFeatureUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    feature = db.query(FleetFeature).filter(FleetFeature.id == feature_id).first()
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(feature, key, value)
    db.commit()
    db.refresh(feature)
    return feature


@router.delete("/features/{feature_id}")
def delete_feature(feature_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    feature = db.query(FleetFeature).filter(FleetFeature.id == feature_id).first()
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found")
    db.delete(feature)
    db.commit()
    return {"detail": "Feature deleted"}
