from pydantic import BaseModel


class InputFlightData(BaseModel):
    from_country: str = None
    to_country: str = None
    departure_date: str = None
    back_date: str = None
    adult_passengers_count: int = 1
    teenager_passengers_count: int = 0
    child_passengers_count: int = 0
    no_back_ticket: bool = False
    is_business_class: bool = False
