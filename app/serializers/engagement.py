from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class EngagementUserResponse(BaseModel):
    id: UUID
    name: str
    age: int
    height: int
    marital_status: str
    nationality: str
    city: Optional[str] 
    religion: str
    caste_community: str
    mother_tongue: str
    education_level: str
    job_title: str
    company_name: str
    annual_income: float
    family_type: str
    fathers_occupation: str
    mothers_occupation: str
    siblings: int
    family_values: str
    dietary_preference: str
    smoking_habit: str
    drinking_habit: str
    hobbies: list[str]
    image: str
    financial_info: Optional[dict] = None

class MatchedUserResponse(BaseModel):
    id: UUID
    name: str
    image: str
