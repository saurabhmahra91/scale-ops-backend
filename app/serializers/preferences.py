from pydantic import BaseModel
from typing import Optional, List

class PreferenceBase(BaseModel):
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    min_height_centimeters: Optional[float] = None
    max_height_centimeters: Optional[float] = None
    gender: Optional[str] = None
    marital_statuses: Optional[List[str]] = None
    religion: Optional[str] = None
    education_levels: Optional[List[str]] = None
    family_types: Optional[List[str]] = None
    dietary_preferences: Optional[List[str]] = None
    smoking_habits: Optional[List[str]] = None
    drinking_habits: Optional[List[str]] = None
    caste_communities: Optional[List[str]] = None
    mother_tongue: Optional[str] = None
    profession: Optional[str] = None
    family_values: Optional[List[str]] = None
    hobbies: Optional[List[str]] = None
    nationality: Optional[str] = None
    willing_to_relocate: Optional[bool] = None

class PreferenceCreate(PreferenceBase):
    min_age: int
    max_age: int
    min_height_centimeters: float
    max_height_centimeters: float
    gender: str
    marital_statuses: List[str]
    religion: str
    education_levels: List[str]
    family_types: List[str]
    dietary_preferences: List[str]
    smoking_habits: List[str]
    drinking_habits: List[str]
    caste_communities: List[str]
    mother_tongue: str
    profession: str
    family_values: List[str]
    hobbies: List[str]
    nationality: str
    willing_to_relocate: bool

class PreferenceUpdate(PreferenceBase):
    pass

class PreferenceResponse(PreferenceBase):
    class Config:
        orm_mode = True
        from_attributes = True
