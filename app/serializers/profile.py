from datetime import date
from decimal import Decimal
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class ProfileBase(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
    bio: Optional[str] = None
    height: Optional[int] = None
    city: Optional[str] = None
    address: Optional[str] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    nationality: Optional[str] = None
    religion: Optional[str] = None
    caste_community: Optional[str] = None
    mother_tongue: Optional[str] = None
    education_level: Optional[str] = None
    college_attended: Optional[str] = None
    job_title: Optional[str] = None
    company_name: Optional[str] = None
    annual_income: Optional[Decimal] = None
    family_type: Optional[str] = None
    fathers_occupation: Optional[str] = None
    mothers_occupation: Optional[str] = None
    siblings: Optional[int] = None
    family_values: Optional[str] = None
    dietary_preference: Optional[str] = None
    smoking_habit: Optional[str] = None
    drinking_habit: Optional[str] = None
    hobbies: Optional[List[str]] = None


class ProfileCreate(ProfileBase):
    name: str
    dob: date
    bio: str
    height: int
    city: str
    address: str
    gender: str
    marital_status: str
    nationality: str
    religion: str
    caste_community: str
    mother_tongue: str
    education_level: str
    family_type: str
    fathers_occupation: str
    mothers_occupation: str
    siblings: int
    family_values: str
    dietary_preference: str
    smoking_habit: str
    drinking_habit: str
    hobbies_interests: List[str]


class ProfileUpdate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    id: UUID

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, obj):
        data = {
            "smoking_habit": obj.smoking_habit,
            "drinking_habit": obj.drinking_habit,
            "dietary_preference": obj.dietary_preference,
            "family_type": obj.family_type,
            "education_level": obj.education_level,
            "nationality": obj.nationality,
            "religion": obj.religion,
            "gender": obj.gender,
            "marital_status": obj.marital_status,
            "id": obj.id,
            "name": obj.name,
            "bio": obj.bio,
            "height": obj.height,
            "dob": obj.dob.isoformat(),
            "city": obj.city,
            "address": obj.address,
            "mobile": obj.mobile,
            "hobbies_interests": obj.hobbies,
            "fathers_occupation": obj.fathers_occupation,
            "mothers_occupation": obj.mothers_occupation,
            "siblings": obj.siblings,
            "family_values": obj.family_values,
            "annual_income": obj.annual_income,
            "image": obj.image,
        }
        return cls(**data)


