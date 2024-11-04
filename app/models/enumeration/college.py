import json
from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values
from unidecode import unidecode
from pathlib import Path


class College(Model):
    id = CharField(unique=True, index=True, primary_key=True, null=True)
    # country = ForeignKeyField(Nationality, backref='colleges')

    class Meta:
        database = db


initialize_database([College])


_values = []

with open(Path(__file__).parent / "colleges.jsonl", "r") as f:
    for line in f:
        data = json.loads(line)
        _values.append(data["college"])

_values = [unidecode(v) for v in _values]
_values = list(set(_values))
insert_enum_values(College, _values)
