from pydantic import BaseModel

class Alert(BaseModel):
    expected: float
    predicted: float
    type: str
