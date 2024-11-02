import json
from peewee import ForeignKeyField, IntegerField, FloatField, CharField, BooleanField, TextField
from app.core.database import db
from app.models.user import User
from .base import BaseModel

from app.core.database import initialize_database
from .profile_enums import MaritalStatus, Religions


class JSONField(TextField):
    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)


class Preferences(BaseModel):
    user = ForeignKeyField(User, backref="preferences", unique=True)
    min_age = IntegerField()
    max_age = IntegerField()
    min_height_centimeters = FloatField()
    max_height_centimeters = FloatField()
    preferred_marital_status = CharField(choices=[(tag.value, tag.name) for tag in MaritalStatus])
    preferred_religion = CharField(choices=[(tag.value, tag.name) for tag in Religions])
    preferred_communities = JSONField(default=[])
    preferred_mother_tongues = JSONField(default=[])
    preferred_education_levels = JSONField(default=[])
    preferred_occupations = JSONField(default=[])
    preferred_countries = JSONField(default=[])
    willing_to_relocate = BooleanField()

    class Meta:
        database = db

    def set_preferred_communities(self, communities):
        self.preferred_communities = communities

    def get_preferred_communities(self):
        return self.preferred_communities

    def set_preferred_mother_tongues(self, mother_tongues):
        self.preferred_mother_tongues = mother_tongues

    def get_preferred_mother_tongues(self):
        return self.preferred_mother_tongues

    def set_preferred_education_levels(self, education_levels):
        self.preferred_education_levels = education_levels

    def get_preferred_education_levels(self):
        return self.preferred_education_levels

    def set_preferred_occupations(self, occupations):
        self.preferred_occupations = occupations

    def get_preferred_occupations(self):
        return self.preferred_occupations

    def set_preferred_countries(self, countries):
        self.preferred_countries = countries

    def get_preferred_countries(self):
        return self.preferred_countries


initialize_database([Preferences])
