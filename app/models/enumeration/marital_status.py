from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values

class MaritalStatus(Model):
    id = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db

initialize_database([MaritalStatus])

_values = ['Never Married', 'Divorced', 'Widowed', 'Awaiting Divorce', 'Married']

insert_enum_values(MaritalStatus, _values)