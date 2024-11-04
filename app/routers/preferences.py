from fastapi import APIRouter, HTTPException, Depends
from app.models.preferences import Preferences
from app.models.user import User
from app.auth.injections import get_current_user
from app.serializers.preferences import (
    PreferenceCreate,
    PreferenceResponse,
    PreferenceUpdate,
)

router = APIRouter()


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

    return PreferenceResponse.model_validate(preference)


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

    return PreferenceResponse.model_validate(preference)


@router.patch("/me", response_model=PreferenceResponse)
async def update_my_preferences(preference: PreferenceUpdate, current_user: User = Depends(get_current_user)):
    """
    Update specific fields of the current user's preferences.
    """
    existing_preference = Preferences.get_or_none(Preferences.user_id == current_user["id"])
    if existing_preference is None:
        raise HTTPException(status_code=404, detail="Preferences not found")

    preference_data = preference.dict(exclude_unset=True)

    for key, value in preference_data.items():
        setattr(existing_preference, key, value)

    existing_preference.save()

    return PreferenceResponse.model_validate(preference)


@router.delete("/me", status_code=204)
async def delete_my_preferences(current_user: dict = Depends(get_current_user)):
    """
    Delete the preferences of the current user.
    """
    preference = Preferences.get_or_none(Preferences.user_id == current_user["id"])
    if preference is None:
        raise HTTPException(status_code=404, detail="Preferences not found")

    preference.delete_instance()
