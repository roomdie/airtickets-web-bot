from pydantic import BaseModel
import typing
from .flight_ticket import FlightTicket


class OutputFlightData(BaseModel):
    available_tickets: typing.List[FlightTicket]
