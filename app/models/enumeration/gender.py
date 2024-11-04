from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values

class Gender(Model):
    value = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db

initialize_database([Gender])

_values = ['Male', 'Female']

insert_enum_values(Gender, _values)
