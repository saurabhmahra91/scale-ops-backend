from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values


class Religion(Model):
    id = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db


initialize_database([Religion])

_values = ["Buddhism", "Christianity", "Hinduism", "Islam", "Judaism", "Sikhism", "Atheistic"]

insert_enum_values(Religion, _values)
