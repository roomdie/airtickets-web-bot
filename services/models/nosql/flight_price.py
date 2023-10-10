from pydantic import BaseModel


class FlightPrice(BaseModel):
    value: int = 100
    currency: str = "USD"
