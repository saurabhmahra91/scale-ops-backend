from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.services.auth import (
    get_user,
    create_user,
    generate_otp,
    create_tokens,
    refresh_access_token,
    verify_otp,
)
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.requests import Request
from app.auth.injections import get_current_user

from app.auth.token import TokenPydantic


router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


class mobileNumber(BaseModel):
    mobile: str


class OTPVerification(BaseModel):
    mobile: str
    otp: str


class RefreshToken(BaseModel):
    refresh_token: str


@router.post("/request-otp")
@limiter.limit("2/minute")
async def request_otp(request: Request, mobile_number: mobileNumber):
    otp = generate_otp()
    print("Here is the generated OTP: ", otp)
    return {"message": f"OTP sent to {mobile_number.mobile}"}


@router.post("/verify-otp", response_model=TokenPydantic)
@limiter.limit("2/minute")
async def verify_otp_and_login(request: Request, otp_verification: OTPVerification):
    if not verify_otp(otp_verification.mobile, otp_verification.otp):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid OTP",
        )

    user = get_user(otp_verification.mobile)
    if not user:
        user, created = create_user(otp_verification.mobile)

        if not created:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create user")

    return create_tokens(user.mobile)


@router.post("/refresh-token", response_model=TokenPydantic)
async def refresh_token(refresh_token: RefreshToken):
    return refresh_access_token(refresh_token.refresh_token)


@router.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
