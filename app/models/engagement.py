from app.core.database import db, initialize_database
from .base import BaseModel
from .user import User
from peewee import ForeignKeyField, CharField
from .enums.engagement_action import EngagementAction


class Engagement(BaseModel):
    initiator = ForeignKeyField(User, backref="actions_given", index=True)
    recipient = ForeignKeyField(User, backref="actions_received", index=True)
    action_type = CharField(
        choices=[(tag.value, tag.name) for tag in EngagementAction],
        null=False,
        index=True,
    )

    class Meta:
        database = db
        indexes = ((("initiator", "recipient"), True),)


initialize_database([Engagement])
