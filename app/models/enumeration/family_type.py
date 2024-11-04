from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values


class FamilyType(Model):
    id = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db

initialize_database([FamilyType])

_values = ['Nuclear Family', 'Joint Family', 'Single Parent Family', 'Extended Family', 'Blended Family', 'Childless Family', 'Grandparent Family', 'Foster Family', 'Adoptive Family', 'Living Alone']

insert_enum_values(FamilyType, _values)