from typing import List

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from peewee import Model

from app.auth.injections import get_current_user
from app.models.profile import Profile, User
from app.serializers.profile import ProfileCreate, ProfileResponse, ProfileUpdate
from app.services.profile import save_profile_image

router = APIRouter()


def convert_db_profile_to_response(db_profile: Profile) -> ProfileResponse:
    profile_data = db_profile.__data__.copy()

    def convert_value(value):
        if isinstance(value, Model):
            return value.id  # Return the id of the related model
        elif isinstance(value, list):
            return [convert_value(item) for item in value]  # Process each item in the list
        return value

    # Convert related Peewee models, enum values, and array fields
    for field, value in profile_data.items():
        profile_data[field] = convert_value(value)

    return ProfileResponse(**profile_data)


@router.post("", response_model=ProfileResponse)
async def create_profile(profile: ProfileCreate, current_user: User = Depends(get_current_user)) -> ProfileResponse:
    """
    Create a new profile for an existing user or update an existing profile.

    Args:
        profile (ProfileCreate): The profile data to create or update.
        current_user (User): The current authenticated user, injected by dependency.

    Returns:
        ProfileResponse: The created or updated profile.

    Raises:
        HTTPException: If there is an error during profile creation/update.
    """

    try:
        # Check if the user already has a profile
        existing_profile = Profile.get_or_none(Profile.user == current_user)

        if existing_profile:
            # Update existing profile
            for field, value in profile.model_dump().items():
                setattr(existing_profile, field, value)
            existing_profile.save()
            return convert_db_profile_to_response(existing_profile)
        else:
            # Create new profile for the authenticated user
            profile_data = profile.model_dump()
            db_profile = Profile.create(user=current_user, **profile_data)
            return convert_db_profile_to_response(db_profile)

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
    return convert_db_profile_to_response(profile)


@router.patch("/{profile_id}", response_model=ProfileResponse)
async def update_profile(
    profile_id: int,
    profile: ProfileUpdate,
    current_user: dict = Depends(get_current_user),
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
    return convert_db_profile_to_response(db_profile)


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
    return convert_db_profile_to_response(profile)


@router.put("/image", response_model=ProfileResponse)
async def upload_profile_image(
    image: UploadFile = File(...), current_user: User = Depends(get_current_user)
) -> ProfileResponse:
    """
    Upload an image for the current user's profile.

    Args:
        image (UploadFile): The image file to upload.
        current_user (User): The current authenticated user, injected by dependency.

    Returns:
        ProfileResponse: The updated profile with the new image.

    Raises:
        HTTPException: If the profile is not found or if there's an error during upload.
    """
    profile = Profile.get_or_none(Profile.user == current_user)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found for current user")

    try:
        save_profile_image(profile, image)
        # Reload the profile from the database to get the updated image field
        updated_profile = Profile.get(Profile.id == profile.id)
        return convert_db_profile_to_response(updated_profile)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error uploading image: {str(e)}")
