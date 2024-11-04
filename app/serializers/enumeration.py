from pydantic import BaseModel

class EnumerationSchema(BaseModel):
    id: str

    class Config:
        orm_mode = True

class EnumerationCreate(BaseModel):
    id: str

class EnumerationUpdate(BaseModel):
    id: str

class EnumerationResponse(EnumerationSchema):
    pass