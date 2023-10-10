from pydantic import BaseModel
import typing
from .flight_details import FlightDetails
from .flight_price import FlightPrice
from .flight_status import FlightStatus

class FlightTicket(BaseModel):
    price: FlightPrice
    flight_details: typing.List[FlightDetails]
    status: FlightStatus
