import json
from peewee import (
    ForeignKeyField,
    IntegerField,
    FloatField,
    CharField,
    BooleanField,
    TextField,
)
from app.core.database import db
from app.models.user import User
from .base import BaseModel

from app.core.database import initialize_database
from .enums.profile_enums import MaritalStatus, Religions
from playhouse.postgres_ext import ArrayField
from .enums.profile_enums.caste_communities import CasteCommunity

class StrEnumField(CharField):
    def __init__(self, enum_class, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enum_class = enum_class

    def db_value(self, value):
        if value is None:
            return None
        return value.value if isinstance(value, self.enum_class) else value

    def python_value(self, value):
        return self.enum_class(value) if value is not None else None


class Preferences(BaseModel):
    user = ForeignKeyField(User, backref="preference", unique=True)
    min_age = IntegerField(null=True, default=18)
    max_age = IntegerField(null=True, default=80)
    min_height_centimeters = FloatField(null=True, default=50)
    max_height_centimeters = FloatField(null=True, default=250)
    preferred_marital_status = CharField(
        choices=[(tag.value, tag.name) for tag in MaritalStatus],
        null=True,
        default=MaritalStatus.PREFER_NOT_TO_SAY,
    )
    preferred_religion = CharField(
        choices=[(tag.value, tag.name) for tag in Religions],
        null=True,
        default=Religions.PREFER_NOT_TO_SAY,
    )

    preferred_communities = ArrayField(StrEnumField(CasteCommunity), default=[], null=True)
    preferred_mother_tongues = ArrayField(CharField, default=[], null=True)
    preferred_education_levels = ArrayField(CharField, default=[], null=True)
    preferred_occupations = ArrayField(CharField, default=[], null=True)
    preferred_countries = ArrayField(CharField, default=[], null=True)
    willing_to_relocate = BooleanField(CharField, null=True, default=True)

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
