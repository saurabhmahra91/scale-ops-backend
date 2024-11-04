import json
from app.core.database import db, initialize_database
from peewee import Model, CharField, ForeignKeyField
from .base import insert_enum_values
from .nationality import Nationality

class College(Model):
    value = CharField(unique=True, index=True, primary_key=True, null=True)
    # country = ForeignKeyField(Nationality, backref='colleges')

    class Meta:
        database = db

initialize_database([College])


_values = []
with open("colleges.jsonl", "r") as f:
    for line in f:
        data = json.loads(line)
        _values.append(data['college'])


insert_enum_values(College, _values)