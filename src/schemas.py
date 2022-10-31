from pydantic import BaseModel

class address(BaseModel):
    addressLat: float
    addressLong: float

class retriever(BaseModel):
    addressLat: float
    addressLong: float
    rang: int