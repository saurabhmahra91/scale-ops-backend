from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values

class EducationLevel(Model):
    id = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db

initialize_database([EducationLevel])

_values = ['Primary Education', 'Secondary Education', 'High School Higher Secondary', 'Diploma', 'Bachelors Degree', 'Masters Degree', 'Doctorate Phd', 'Post Doctoral', 'Professional Certification', 'Vocational Training', 'Some College No Degree', 'Associate Degree']

insert_enum_values(EducationLevel, _values)