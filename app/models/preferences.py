from peewee import (
    ForeignKeyField,
    IntegerField,
    FloatField,
    CharField,
    BooleanField,
)
from app.core.database import db
from app.models.user import User
from .base import BaseModel
from .profile import Profile
from app.core.database import initialize_database

from playhouse.postgres_ext import ArrayField
from .enumeration.gender import Gender
from .enumeration.religion import Religion
from .enumeration.nationality import Nationality
from .enumeration.language import Language
from .enumeration.profession import Profession


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
    gender = ForeignKeyField(Gender, null=True, default=None)
    marital_statuses = ArrayField(CharField, null=True)
    religion = ForeignKeyField(Religion, backref="preferences", null=True)
    education_levels = ArrayField(CharField, null=True)
    family_types = ArrayField(CharField, null=True)
    dietary_preferences = ArrayField(CharField, null=True)
    smoking_habits = ArrayField(CharField, null=True)
    drinking_habits = ArrayField(CharField, null=True)
    caste_communities = ArrayField(CharField, null=True)
    mother_tongue = ForeignKeyField(Language, backref="preferences", null=True)
    profession = ForeignKeyField(Profession, backref="preferences", null=True)
    family_values = ArrayField(CharField, null=True)
    hobbies = ArrayField(CharField, null=True)
    nationality = ForeignKeyField(Nationality, backref="preferences", null=True)
    willing_to_relocate = BooleanField(null=False, default=True)

    class Meta:
        database = db

    def save(self, *args, **kwargs):
        user_profile = Profile.get(user=self.user)

        if self.gender is None:
            self.gender = user_profile.gender

        if self.nationality is None:
            self.nationality = user_profile.nationality

        return super().save(*args, **kwargs)


initialize_database([Preferences])
