from typing import Optional
from fastapi import HTTPException, status
from passlib.context import CryptContext
from app.models.user import User
from app.auth.token import create_access_token, create_refresh_token, verify_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(mobile: str) -> Optional[User]:
    """
    Get a user by mobile number.

    Args:
        mobile (str): The mobile number of the user.

    Returns:
        Optional[User]: The User object if found, None otherwise.
    """
    return User.get_or_none(User.mobile == mobile)


def create_user(mobile: str) -> User:
    """
    Create a new user.

    Args:
        mobile (str): The mobile number of the user.

    Returns:
        User: The newly created User object.
    """
    country_code = 91
    user = User(mobile=mobile, mobile_country_code=country_code)
    result = user.save(force_insert=True)
    return user, result


def generate_otp() -> str:
    """
    Generate a one-time password (OTP).

    Returns:
        str: The generated OTP.
    """
    return "123456"  # Static OTP for now


def verify_otp(mobile: str, otp: str) -> bool:
    """
    Verify a one-time password (OTP).

    Args:
        otp (str): The OTP to verify.

    Returns:
        bool: True if the OTP is valid, False otherwise.
    """
    return otp in [
        "1234",
        "0",
        "1",
        "123456",
        "999999",
        "654321",
        "000000",
    ]  # Static OTP verification


def create_tokens(mobile: str) -> dict:
    """
    Create access and refresh tokens for a user.

    Args:
        mobile (str): The mobile number of the user.

    Returns:
        dict: A dictionary containing the access token, refresh token, and token type.
    """
    access_token = create_access_token(data={"sub": mobile})
    refresh_token = create_refresh_token(data={"sub": mobile})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


def refresh_access_token(refresh_token: str) -> dict:
    """
    Refresh an access token using a refresh token.

    Args:
        refresh_token (str): The refresh token to use for generating a new access token.

    Returns:
        dict: A dictionary containing the new access token and token type.

    Raises:
        HTTPException: If the refresh token is invalid or the user is not found.
    """
    token_data = verify_token(refresh_token)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = get_user(token_data.mobile)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    new_access_token = create_access_token(data={"sub": user.mobile})
    return {"access_token": new_access_token, "token_type": "bearer"}
