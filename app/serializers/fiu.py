from pydantic import BaseModel


class ConsentRequest(BaseModel):
    mobile: str
    callback_url: str


class ConsentFetchRequest(BaseModel):
    handle: str
