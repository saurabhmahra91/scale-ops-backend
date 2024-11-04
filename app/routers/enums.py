from app.models.enums.profile_enums import (
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
from fastapi import APIRouter
from app.serializers.enums import EnumItem
from app.services.enum import enum_to_dict

router = APIRouter()


@router.get("/marital-status", response_model=list[EnumItem])
async def get_marital_status():
    """Get all possible values for MaritalStatus enum."""
    return enum_to_dict(MaritalStatus)


@router.get("/religions", response_model=list[EnumItem])
async def get_religions():
    """Get all possible values for Religions enum."""
    return enum_to_dict(Religions)


@router.get("/genders", response_model=list[EnumItem])
async def get_genders():
    """Get all possible values for Genders enum."""
    return enum_to_dict(Genders)


@router.get("/education-levels", response_model=list[EnumItem])
async def get_education_levels():
    """Get all possible values for EducationLevels enum."""
    return enum_to_dict(EducationLevels)


@router.get("/family-types", response_model=list[EnumItem])
async def get_family_types():
    """Get all possible values for FamilyType enum."""
    return enum_to_dict(FamilyType)


@router.get("/dietary-preferences", response_model=list[EnumItem])
async def get_dietary_preferences() -> list[EnumItem]:
    """Get all possible values for DietaryPreferences enum."""
    return enum_to_dict(DietaryPreferences)


@router.get("/smoking-habits", response_model=list[EnumItem])
async def get_smoking_habits():
    """Get all possible values for SmokingHabits enum."""
    return enum_to_dict(SmokingHabits)


@router.get("/drinking-habits", response_model=list[EnumItem])
async def get_drinking_habits():
    """Get all possible values for DrinkingHabits enum."""
    return enum_to_dict(DrinkingHabits)


@router.get("/nationalities", response_model=list[EnumItem])
async def get_nationalities():
    """Get all possible values for Nationalities enum."""
    return enum_to_dict(Nationalities)
