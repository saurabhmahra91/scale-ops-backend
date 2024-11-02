from datetime import datetime

from peewee import (
    Model,
    DateTimeField,
)

from app.core.database import db


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now, index=True)
    updated_at = DateTimeField(default=datetime.now, index=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db
