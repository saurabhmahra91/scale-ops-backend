from datetime import date
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.models.enums.profile_enums import (
    DietaryPreferences,
    DrinkingHabits,
    EducationLevels,
    FamilyType,
    Genders,
    MaritalStatus,
    Nationalities,
    Religions,
    SmokingHabits,
)


class ProfileBase(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
    bio: Optional[str] = None
    height: Optional[int] = None
    city: Optional[str] = None
    address: Optional[str] = None
    gender: Optional[Genders] = None
    marital_status: Optional[MaritalStatus] = None
    nationality: Optional[str] = None
    religion: Optional[str] = None
    caste_community: Optional[str] = None
    mother_tongue: Optional[str] = None
    education_level: Optional[EducationLevels] = None
    college_attended: Optional[str] = None
    job_title: Optional[str] = None
    company_name: Optional[str] = None
    annual_income: Optional[Decimal] = None
    family_type: Optional[FamilyType] = None
    fathers_occupation: Optional[str] = None
    mothers_occupation: Optional[str] = None
    siblings: Optional[int] = None
    family_values: Optional[str] = None
    dietary_preference: Optional[DietaryPreferences] = None
    smoking_habit: Optional[SmokingHabits] = None
    drinking_habit: Optional[DrinkingHabits] = None
    hobbies_interests: Optional[str] = None


class ProfileCreate(ProfileBase):
    name: str
    dob: date
    bio: str
    height: int
    city: str
    address: str
    gender: Genders
    marital_status: MaritalStatus
    nationality: Nationalities
    religion: Religions
    caste_community: str
    mother_tongue: str
    education_level: EducationLevels
    family_type: FamilyType
    fathers_occupation: str
    mothers_occupation: str
    siblings: int
    family_values: str
    dietary_preference: DietaryPreferences
    smoking_habit: SmokingHabits
    drinking_habit: DrinkingHabits
    hobbies_interests: str


class ProfileUpdate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    id: UUID

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, obj):
        data = {
            "smoking_habit": obj.smoking_habit_enum.name if obj.smoking_habit_enum else None,
            "drinking_habit": obj.drinking_habit_enum.name if obj.drinking_habit_enum else None,
            "dietary_preference": obj.dietary_preference_enum.name if obj.dietary_preference_enum else None,
            "family_type": obj.family_type_enum.name if obj.family_type_enum else None,
            "education_level": obj.education_level_enum.name if obj.education_level_enum else None,
            "nationality": obj.nationality_enum.name if obj.nationality_enum else None,
            "religion": obj.religion_enum.name if obj.religion_enum else None,
            "gender": obj.gender_enum.name if obj.gender_enum else None,
            "marital_status": obj.marital_status_enum.name if obj.marital_status_enum else None,
            "id": obj.id,
            "name": obj.name,
            "bio": obj.bio,
            "height": obj.height,
            "dob": obj.dob.isoformat(),
            "city": obj.city,
            "address": obj.address,
            "mobile": obj.mobile,
            "hobbies_interests": obj.hobbies_interests,
            "fathers_occupation": obj.fathers_occupation,
            "mothers_occupation": obj.mothers_occupation,
            "siblings": obj.siblings,
            "family_values": obj.family_values,
            "annual_income": obj.annual_income,
            "image": obj.image,
        }
        return cls(**data)
