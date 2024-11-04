from pydantic import BaseModel


class MobileNumber(BaseModel):
    mobile: str


class OTPVerification(BaseModel):
    mobile: str
    otp: str


class RefreshToken(BaseModel):
    refresh_token: str
