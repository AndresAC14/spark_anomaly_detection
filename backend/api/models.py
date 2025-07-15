from pydantic import BaseModel

class Alert(BaseModel):
    expected: float
    predicted: float
    type: str
    hour: int

class DataPoint(BaseModel):
    expected: float
    predicted: float
    type: str
    hour: int
