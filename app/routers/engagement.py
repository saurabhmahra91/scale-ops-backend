from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.engagement import Engagement
from app.models.user import User
from app.serializers.engagement import EngagementCreate, EngagementResponse

router = APIRouter()


@router.post("/engagements/", response_model=EngagementResponse)
def create_engagement(engagement: EngagementCreate, db: Session = Depends(get_db)):
    db_engagement = Engagement(**engagement.dict())
    db.add(db_engagement)
    db.commit()
    db.refresh(db_engagement)
    return db_engagement


@router.get("/engagements/", response_model=List[EngagementResponse])
def read_engagements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    engagements = db.query(Engagement).offset(skip).limit(limit).all()
    return engagements


@router.get("/engagements/{engagement_id}", response_model=EngagementResponse)
def read_engagement(engagement_id: int, db: Session = Depends(get_db)):
    engagement = db.query(Engagement).filter(Engagement.id == engagement_id).first()
    if engagement is None:
        raise HTTPException(status_code=404, detail="Engagement not found")
    return engagement


@router.put("/engagements/{engagement_id}", response_model=EngagementResponse)
def update_engagement(engagement_id: int, engagement: EngagementCreate, db: Session = Depends(get_db)):
    db_engagement = db.query(Engagement).filter(Engagement.id == engagement_id).first()
    if db_engagement is None:
        raise HTTPException(status_code=404, detail="Engagement not found")

    for key, value in engagement.dict().items():
        setattr(db_engagement, key, value)

    db.commit()
    db.refresh(db_engagement)
    return db_engagement


@router.delete("/engagements/{engagement_id}", response_model=EngagementResponse)
def delete_engagement(engagement_id: int, db: Session = Depends(get_db)):
    engagement = db.query(Engagement).filter(Engagement.id == engagement_id).first()
    if engagement is None:
        raise HTTPException(status_code=404, detail="Engagement not found")

    db.delete(engagement)
    db.commit()
    return engagement


@router.get("/users/{user_id}/engagements/given", response_model=List[EngagementResponse])
def read_user_engagements_given(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.actions_given


@router.get("/users/{user_id}/engagements/received", response_model=List[EngagementResponse])
def read_user_engagements_received(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.actions_received
