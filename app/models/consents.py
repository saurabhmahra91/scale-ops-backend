from peewee import ForeignKeyField, UUIDField

from app.core.database import initialize_database
from .base import BaseModel
from .user import User
import uuid


class UserConsentRequests(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, index=True, null=False)
    user = ForeignKeyField(User, backref="consent_requests", index=True, null=False)
    consent_handle = UUIDField(unique=True, index=True, null=False)

    class Meta:
        table_name = "user_consent_requests"


initialize_database([UserConsentRequests])
