from app.models.engagement import ActionType
from pydantic import BaseModel
from datetime import datetime


class EngagementCreate(BaseModel):
    initiator_id: int
    recipient_id: int
    action_type: ActionType


class EngagementResponse(BaseModel):
    id: int
    initiator_id: int
    recipient_id: int
    action_type: ActionType
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
