from fastapi import Depends, HTTPException, status

from app.models.user import User
from app.services.auth import get_user, verify_token

from .config import oauth2_scheme


async def get_current_user(token: str = Depends(oauth2_scheme)):
    token_data = verify_token(token)
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = get_user(token_data.mobile)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def is_admin(current_user: dict = Depends(get_current_user)):
    """
    Dependency to check if the current user is an admin.

    Args:
        current_user (dict): The current user, obtained from the get_current_user dependency.

    Returns:
        User: The current user if they are an admin.

    Raises:
        HTTPException: If the user is not an admin.
    """
    user = User.get_or_none(User.id == current_user["id"])
    if not user or not user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="The user doesn't have enough privileges")
    return user
