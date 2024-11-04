from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values

class DietaryPreference(Model):
    value = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db

initialize_database([DietaryPreference])

_values = ['Vegetarian', 'Vegan', 'Pescatarian', 'Omnivore', 'Keto', 'Paleo', 'Gluten Free', 'Dairy Free', 'Halal', 'Kosher', 'Low Carb', 'Low Fat', 'Organic', ]

insert_enum_values(DietaryPreference, _values)