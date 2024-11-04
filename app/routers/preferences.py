from fastapi import APIRouter, HTTPException, Depends
from app.models.preferences import Preferences
from app.models.user import User
from app.auth.injections import get_current_user
from app.serializers.preferences import (
    PreferenceCreate,
    PreferenceResponse,
    PreferenceUpdate,
)
from peewee import Model

router = APIRouter()


def convert_db_preference_to_response(db_preference: Preferences) -> PreferenceResponse:
    preference_data = db_preference.__data__.copy()

    def convert_value(value):
        if isinstance(value, Model):
            return value.id  # Return the id of the related model
        elif isinstance(value, list):
            return [convert_value(item) for item in value]  # Process each item in the list
        return value

    # Convert related Peewee models, enum values, and array fields
    for field, value in preference_data.items():
        preference_data[field] = convert_value(value)

    return PreferenceResponse(**preference_data)


@router.get("/me", response_model=PreferenceResponse)
async def get_my_preferences(current_user: User = Depends(get_current_user)):
    """
    Get the preferences of the current user.
    If none exist, create a default one.
    """
    preference = Preferences.get_or_none(Preferences.user == current_user)
    if preference is None:
        # Create a default preference for the user
        preference = Preferences.create(user=current_user)

    return convert_db_preference_to_response(preference)


@router.post("/me", response_model=PreferenceResponse)
async def create_or_update_my_preferences(preference: PreferenceCreate, current_user: User = Depends(get_current_user)):
    """
    Create or update the preferences of the current user.
    """
    user = User.get_by_id(current_user.id)
    preference_data = preference.model_dump()
    existing_preference, created = Preferences.get_or_create(user=user)

    for key, value in preference_data.items():
        setattr(existing_preference, key, value)

    existing_preference.save()

    return convert_db_preference_to_response(existing_preference)


@router.patch("/me", response_model=PreferenceResponse)
async def update_my_preferences(preference: PreferenceUpdate, current_user: User = Depends(get_current_user)):
    """
    Update specific fields of the current user's preferences.
    """
    existing_preference = Preferences.get_or_none(Preferences.user_id == current_user.id)
    if existing_preference is None:
        raise HTTPException(status_code=404, detail="Preferences not found")

    preference_data = preference.dict(exclude_unset=True)

    for key, value in preference_data.items():
        setattr(existing_preference, key, value)

    existing_preference.save()

    return convert_db_preference_to_response(existing_preference)


@router.delete("/me", status_code=204)
async def delete_my_preferences(current_user: User = Depends(get_current_user)):
    """
    Delete the preferences of the current user.
    """
    preference = Preferences.get_or_none(Preferences.user_id == current_user.id)
    if preference is None:
        raise HTTPException(status_code=404, detail="Preferences not found")

    preference.delete_instance()
    return convert_db_preference_to_response(preference)
