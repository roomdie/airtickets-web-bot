from pydantic import BaseModel


class FlightDetails(BaseModel):
    company: str
    flight_code: str
    from_country: str
    to_country: str
    departure_airport: str
    arrival_airport: str
    departure_date: str
    arrival_date: str
    departure_time: int
    arrival_time: int
    duration: int
    is_back_ticket: bool
    gate: str
    passenger_seat: str
    passenger_class: str
