from pydantic import BaseModel

class address(BaseModel):
    addressLat: float
    addressLong: float