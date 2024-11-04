from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values

class DrinkingHabit(Model):
    id = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db

initialize_database([DrinkingHabit])

_values = ['Non Drinker', 'Occasional Drinker', 'Social Drinker', 'Regular Drinker', 'Trying To Quit']

insert_enum_values(DrinkingHabit, _values)