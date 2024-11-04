from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.auth.injections import get_current_user, is_admin
from app.models.user import User
from app.serializers.user import UserCreate, UserResponse, UserUpdate

router = APIRouter()


@router.post("", response_model=UserResponse)
async def create_user(user: UserCreate, current_user: User = Depends(is_admin)) -> UserResponse:
    """
    Create a new user.

    Args:
        user (UserCreate): The user data to create.
        current_user (User): The current user, must be an admin.

    Returns:
        UserResponse: The created user.
    """
    db_user = User.create(**user.dict())
    return db_user


@router.get("", response_model=List[UserResponse])
async def read_users(
    current_user: User = Depends(get_current_user),
) -> List[UserResponse]:
    """
    Retrieve a list of all users.

    Args:
        current_user (User): The current user, must be active.

    Returns:
        List[UserResponse]: A list of users.
    """
    return list(User.select())


@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: str, current_user: User = Depends(get_current_user)) -> UserResponse:
    """
    Retrieve a user by ID.

    Args:
        user_id (str): The ID of the user to retrieve.
        current_user (User): The current user, must be active.

    Returns:
        UserResponse: The user with the specified ID.

    Raises:
        HTTPException: If the user is not found.
    """
    user = User.get_or_none(User.id == user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user: UserUpdate, current_user: User = Depends(is_admin)) -> UserResponse:
    """
    Update a user by ID.

    Args:
        user_id (str): The ID of the user to update.
        user (UserUpdate): The user data to update.
        current_user (User): The current user, must be an admin.

    Returns:
        UserResponse: The updated user.

    Raises:
        HTTPException: If the user is not found.
    """
    db_user = User.get_or_none(User.id == user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db_user.save()
    return db_user


@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: str, current_user: User = Depends(is_admin)) -> UserResponse:
    """
    Delete a user by ID.

    Args:
        user_id (str): The ID of the user to delete.
        current_user (User): The current user, must be an admin.

    Returns:
        UserResponse: The deleted user.

    Raises:
        HTTPException: If the user is not found.
    """
    user = User.get_or_none(User.id == user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.delete_instance()
    return user
