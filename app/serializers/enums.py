from pydantic import BaseModel


class EnumItem(BaseModel):
    name: str
    value: int
