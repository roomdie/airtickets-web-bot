from pydantic import BaseModel


class FlightStatus(BaseModel):
    name: str
    color: str = None
    emoji: str = None
