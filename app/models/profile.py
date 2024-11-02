from peewee import CharField, DateField, DecimalField, IntegerField, TextField, UUIDField
import uuid
from app.core.database import db, initialize_database

from .base import BaseModel
from .profile_enums import (
    MaritalStatus,
    Religions,
    Genders,
    EducationLevels,
    FamilyType,
    DietaryPreferences,
    SmokingHabits,
    DrinkingHabits,
    Nationalities,
)


class Profile(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, index=True, null=False)
    name = CharField(null=False, max_length=32)
    dob = DateField(null=True, index=True)
    city = CharField(index=True, null=True)
    address = TextField(null=True)
    gender = IntegerField(choices=[(tag.value, tag.name) for tag in Genders], index=True, null=True)
    marital_status = IntegerField(choices=[(tag.value, tag.name) for tag in MaritalStatus], index=True, null=True)
    nationality = CharField(choices=[(tag.value, tag.name) for tag in Nationalities], index=True, null=True)
    religion = CharField(choices=[(tag.value, tag.name) for tag in Religions], index=True, null=True)
    caste_community = CharField(null=True)
    mother_tongue = CharField(null=True)
    education_level = CharField(choices=[(tag.value, tag.name) for tag in EducationLevels], index=True, null=True)
    college_attended = CharField(null=True, index=True)
    job_title = CharField(null=True, index=True)
    company_name = CharField(null=True, index=True)
    annual_income = DecimalField(decimal_places=2, null=True, index=True)
    family_type = CharField(choices=[(tag.value, tag.name) for tag in FamilyType], index=True, null=True)
    fathers_occupation = CharField(null=True)
    mothers_occupation = CharField(null=True)
    siblings = IntegerField(null=True)
    family_values = CharField(null=True)
    dietary_preference = CharField(choices=[(tag.value, tag.name) for tag in DietaryPreferences], index=True, null=True)
    smoking_habit = CharField(choices=[(tag.value, tag.name) for tag in SmokingHabits], index=True, null=True)
    drinking_habit = CharField(choices=[(tag.value, tag.name) for tag in DrinkingHabits], index=True, null=True)
    hobbies_interests = TextField()

    class Meta:
        database = db

    @property
    def gender_enum(self):
        return Genders(self.gender) if self.gender else None

    @gender_enum.setter
    def gender_enum(self, value):
        self.gender = value.value if value else None

    @property
    def marital_status_enum(self):
        return MaritalStatus(self.marital_status) if self.marital_status else None

    @marital_status_enum.setter
    def marital_status_enum(self, value):
        self.marital_status = value.value if value else None

    @property
    def nationality_enum(self):
        return Nationalities(self.nationality) if self.nationality else None

    @nationality_enum.setter
    def nationality_enum(self, value):
        self.nationality = value.value if value else None

    @property
    def religion_enum(self):
        return Religions(self.religion) if self.religion else None

    @religion_enum.setter
    def religion_enum(self, value):
        self.religion = value.value if value else None

    @property
    def education_level_enum(self):
        return EducationLevels(self.education_level) if self.education_level else None

    @education_level_enum.setter
    def education_level_enum(self, value):
        self.education_level = value.value if value else None

    @property
    def family_type_enum(self):
        return FamilyType(self.family_type) if self.family_type else None

    @family_type_enum.setter
    def family_type_enum(self, value):
        self.family_type = value.value if value else None

    @property
    def dietary_preference_enum(self):
        return DietaryPreferences(self.dietary_preference) if self.dietary_preference else None

    @dietary_preference_enum.setter
    def dietary_preference_enum(self, value):
        self.dietary_preference = value.value if value else None

    @property
    def smoking_habit_enum(self):
        return SmokingHabits(self.smoking_habit) if self.smoking_habit else None

    @smoking_habit_enum.setter
    def smoking_habit_enum(self, value):
        self.smoking_habit = value.value if value else None

    @property
    def drinking_habit_enum(self):
        return DrinkingHabits(self.drinking_habit) if self.drinking_habit else None

    @drinking_habit_enum.setter
    def drinking_habit_enum(self, value):
        self.drinking_habit = value.value if value else None


initialize_database([Profile])
