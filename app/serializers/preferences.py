from pydantic import BaseModel
from typing import Optional
from app.models.enums.profile_enums import (
    MaritalStatus,
    Religions,
    EducationLevels,
    Nationalities,
)


class PreferenceBase(BaseModel):
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    min_height_centimeters: Optional[float] = None
    max_height_centimeters: Optional[float] = None
    preferred_marital_status: Optional[MaritalStatus] = None
    preferred_religion: Optional[Religions] = None
    preferred_communities: Optional[list[str]] = []
    preferred_mother_tongues: Optional[list[str]] = []
    preferred_education_levels: Optional[list[EducationLevels]] = []
    preferred_occupations: Optional[list[str]] = []
    preferred_countries: Optional[list[Nationalities]] = []
    willing_to_relocate: Optional[bool] = None


class PreferenceCreate(PreferenceBase):
    min_age: int
    max_age: int
    min_height_centimeters: float
    max_height_centimeters: float
    preferred_marital_status: MaritalStatus
    preferred_religion: Religions
    preferred_communities: list[str]
    preferred_mother_tongues: list[str]
    preferred_education_levels: list[EducationLevels]
    preferred_occupations: list[str]
    preferred_countries: list[Nationalities]
    willing_to_relocate: bool


class PreferenceUpdate(PreferenceBase):
    pass


class PreferenceResponse(PreferenceBase):
    class Config:
        orm_mode = True
        from_attributes = True
