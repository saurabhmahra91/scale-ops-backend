from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values


class FamilyValue(Model):
    id = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db


initialize_database([FamilyValue])

_values = [
    "Traditionalist",
    "Independent",
    "Collectivist",
    "Progressive",
    "Religious or Spiritual",
    "Career-Oriented",
    "Supportive",
    "Financially-Conservative",
    "Open-Communication",
    "Health-Conscious",
]


insert_enum_values(FamilyValue, _values)
