from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values


class SmokingHabit(Model):
    id = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db


initialize_database([SmokingHabit])

_values = ['Non Smoker', 'Occasional Smoker', 'Regular Smoker', 'Trying To Quit']

insert_enum_values(SmokingHabit, _values)