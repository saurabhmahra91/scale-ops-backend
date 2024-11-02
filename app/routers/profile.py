from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from app.models.profile import Profile
from app.models.profile_enums import (
    MaritalStatus,
    Genders,
    EducationLevels,
    FamilyType,
    DietaryPreferences,
    SmokingHabits,
    DrinkingHabits,
)

from app.auth.injections import get_current_user

router = APIRouter()


class ProfileBase(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
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
    city: str
    address: str
    gender: Genders
    marital_status: MaritalStatus
    nationality: str
    religion: str
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
        }
        return cls(**data)


@router.post("", response_model=ProfileResponse)
async def create_profile(profile: ProfileCreate, current_user: dict = Depends(get_current_user)) -> ProfileResponse:
    """
    Create a new profile.

    Args:
        profile (ProfileCreate): The profile data to create.
        current_user (dict): The current active user, injected by dependency.

    Returns:
        ProfileResponse: The created profile.

    Raises:
        HTTPException: If there is an error during profile creation.
    """
    try:
        db_profile = Profile.create(**profile.model_dump())
        return db_profile
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=List[ProfileResponse])
async def read_profiles(current_user: dict = Depends(get_current_user)) -> List[ProfileResponse]:
    """
    Retrieve the profiles for the current user.

    Args:
        current_user (dict): The current active user, injected by dependency.

    Returns:
        List[ProfileResponse]: A list of all profiles.
    """
    return list(Profile.select())


@router.get("/{profile_id}", response_model=ProfileResponse)
async def read_profile(profile_id: int, current_user: dict = Depends(get_current_user)) -> ProfileResponse:
    """
    Retrieve a profile by ID.

    Args:
        profile_id (int): The ID of the profile to retrieve.
        current_user (dict): The current active user, injected by dependency.

    Returns:
        ProfileResponse: The profile with the specified ID.

    Raises:
        HTTPException: If the profile is not found.
    """
    profile = Profile.get_or_none(Profile.id == profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.patch("/{profile_id}", response_model=ProfileResponse)
async def update_profile(
    profile_id: int, profile: ProfileUpdate, current_user: dict = Depends(get_current_user)
) -> ProfileResponse:
    """
    Update a profile by ID.

    Args:
        profile_id (int): The ID of the profile to update.
        profile (ProfileUpdate): The profile data to update.
        current_user (dict): The current active user, injected by dependency.

    Returns:
        ProfileResponse: The updated profile.

    Raises:
        HTTPException: If the profile is not found.
    """
    db_profile = Profile.get_or_none(Profile.id == profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    update_data = profile.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_profile, field, value)

    db_profile.save()
    return db_profile


@router.delete("/{profile_id}", response_model=ProfileResponse)
async def delete_profile(profile_id: int, current_user: dict = Depends(get_current_user)) -> ProfileResponse:
    """
    Delete a profile by ID.

    Args:
        profile_id (int): The ID of the profile to delete.
        current_user (dict): The current active user, injected by dependency.

    Returns:
        ProfileResponse: The deleted profile.

    Raises:
        HTTPException: If the profile is not found.
    """
    profile = Profile.get_or_none(Profile.id == profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    profile.delete_instance()
    return profile
