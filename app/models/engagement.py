from app.core.database import db, initialize_database
from .base import BaseModel
from .user import User
from peewee import ForeignKeyField, BooleanField, UUIDField
from uuid import uuid4


class Engagement(BaseModel):
    id = UUIDField(primary_key=True, default=uuid4, index=True, null=False)
    initiator = ForeignKeyField(User, backref="actions_given", index=True, null=False)
    recipient = ForeignKeyField(User, backref="actions_received", index=True, null=False)
    action = BooleanField(null=False)

    class Meta:
        database = db
        indexes = ((("initiator", "recipient"), True),)


initialize_database([Engagement])
