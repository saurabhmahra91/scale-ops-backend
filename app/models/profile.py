from peewee import (
    CharField,
    DateField,
    DecimalField,
    IntegerField,
    TextField,
    UUIDField,
    ForeignKeyField,
)
from playhouse.postgres_ext import ArrayField
import uuid
from app.core.database import db, initialize_database
from playhouse.postgres_ext import JSONField
from .base import BaseModel


from .enumeration.gender import Gender
from .enumeration.marital_status import MaritalStatus
from .enumeration.religion import Religion
from .enumeration.education_level import EducationLevel
from .enumeration.family_type import FamilyType
from .enumeration.dietary_preference import DietaryPreference
from .enumeration.smoking_habit import SmokingHabit
from .enumeration.drinking_habit import DrinkingHabit
from .enumeration.nationality import Nationality
from .enumeration.caste_community import CasteCommunity
from .enumeration.language import Language
from .enumeration.college import College
from .enumeration.profession import Profession
from .enumeration.family_values import FamilyValue
from .enumeration.hobby import Hobby
from .user import User


class Profile(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, index=True, null=False)
    user = ForeignKeyField(User, backref="user", unique=True)
    name = CharField(null=False, max_length=32)
    bio = CharField(max_length=8192, null=False)
    dob = DateField(null=True, index=True)
    height = IntegerField(null=True, index=True)
    city = CharField(index=True, null=True)
    image = CharField(null=True)
    images = ArrayField(TextField, null=True)
    address = TextField(null=True)

    gender = ForeignKeyField(model=Gender, backref="profiles")
    religion = ForeignKeyField(model=Religion, backref="profiles")
    caste_community = ForeignKeyField(model=CasteCommunity, backref="profiles")
    mother_tongue = ForeignKeyField(model=Language, backref="profiles")
    education_level = ForeignKeyField(model=EducationLevel, backref="profiles")
    college_attended = ForeignKeyField(model=College, backref="profiles")
    marital_status = ForeignKeyField(model=MaritalStatus, backref="profiles")
    nationality = ForeignKeyField(model=Nationality, backref="profiles", default="India")
    job_title = ForeignKeyField(model=Profession, backref="profiles")
    company_name = CharField(null=True, index=True)
    annual_income = DecimalField(decimal_places=2, null=True, index=True)
    family_type = ForeignKeyField(model=FamilyType, backref="profiles")
    fathers_occupation = ForeignKeyField(model=Profession, backref="profiles")
    mothers_occupation = ForeignKeyField(model=Profession, backref="profiles")
    siblings = IntegerField(null=True)
    family_values = ForeignKeyField(model=FamilyValue, backref="profiles")
    dietary_preference = ForeignKeyField(model=DietaryPreference, backref="profiles")
    smoking_habit = ForeignKeyField(model=SmokingHabit, backref="profiles")
    drinking_habit = ForeignKeyField(model=DrinkingHabit, backref="profiles")
    hobbies_interests = ArrayField(CharField, default=[], null=False)

    financial_info = JSONField(null=True)

    class Meta:
        database = db


initialize_database([Profile])
