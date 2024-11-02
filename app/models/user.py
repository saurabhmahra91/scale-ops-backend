from peewee import CharField, BooleanField, UUIDField, IntegerField
from .base import BaseModel
from app.core.database import initialize_database
import uuid


class User(BaseModel):
    id = UUIDField(primary_key=True, index=True, default=uuid.uuid4)
    mobile = CharField(index=True, null=False)
    mobile_country_code = IntegerField(null=False)
    is_verified = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    is_deleted = BooleanField(default=False)

    class Meta:
        indexes = (
            # Create a unique index on mobile and is_verified
            (("mobile", "is_verified"), True),
        )


initialize_database([User])
