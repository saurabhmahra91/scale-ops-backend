from pydantic import BaseModel


class UserBase(BaseModel):
    mobile: str
    is_verified: bool = False
    is_active: bool = True
    is_admin: bool = False
    is_deleted: bool = False


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: str
