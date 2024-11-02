from fastapi import APIRouter, Depends, HTTPException, status
from app.services.auth import (
    get_user,
    create_user,
    create_tokens,
    verify_otp,
)
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.requests import Request

from fastapi.security import OAuth2PasswordRequestForm
from .token import TokenPydantic


router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@router.post("/token", response_model=TokenPydantic)
@limiter.limit("2/minute")
async def login_for_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    mobile = form_data.username  # In this case, username is the mobile number
    otp = form_data.password  # Password field is used for OTP

    if not verify_otp(mobile, otp):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid OTP",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = get_user(mobile)
    if not user:
        user, created = create_user(mobile)

        if not created:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create user")

    return create_tokens(user.mobile)
