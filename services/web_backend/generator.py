from services import models
import random
import string
import constants


class FlightGenerator:
    def __init__(
            self, from_country: str, to_country: str,
            adult_passengers_count: int, teenager_passengers_count: int,
            child_passengers_count: int, is_business_class: bool, departure_date,
            back_date=None, no_back_ticket=False,
    ):
        self.from_country = from_country
        self.to_country = to_country
        self.is_business_class = is_business_class
        self.adult_passengers_count = adult_passengers_count
        self.teenager_passengers_count = teenager_passengers_count
        self.child_passengers_count = child_passengers_count
        self.departure_date = departure_date
        self.back_date = back_date
        self.no_back_ticket = no_back_ticket

    def generate_gate(self):
        letters = random.choices(string.ascii_uppercase, k=1)
        numbers = random.choices(string.digits, k=2)
        return ''.join(letters + numbers)

    def generate_seat(self):
        numbers = random.choices(string.digits, k=1)
        letters = random.choices(string.ascii_uppercase, k=1)
        return ''.join(numbers + letters)

    def generate_class(self):
        _class = random.choices(string.ascii_uppercase, k=1)
        return ''.join(_class)

    def generate_flight_code(self):
        letters = random.choices(string.ascii_uppercase, k=2)
        numbers = random.choices(string.digits, k=3)
        return ''.join(letters + numbers)

    def get_country_airport(self, country):
        for c in constants.COUNTRIES:
            if c["country"] == country:
                return c["airport"]

    def generate_flights(self):
        available_tickets = []

        # Generate 3-6 random flights
        num_flights = random.randint(3, 6)
        for _ in range(num_flights):
            flight_details = []

            departure_time = random.choice([10, 12, 14])
            arrival_time = random.choice([18, 20, 22])
            duration = arrival_time - departure_time

            departure_airport = self.get_country_airport(self.from_country)
            arrival_airport = self.get_country_airport(self.to_country)
            flight = models.nosql.FlightDetails(
                company=random.choice(constants.AIRLINE_COMPANIES),
                flight_code=self.generate_flight_code(),
                from_country=self.from_country,
                to_country=self.to_country,
                departure_airport=departure_airport,
                arrival_airport=arrival_airport,
                departure_date=self.departure_date,
                arrival_date=self.departure_date,
                departure_time=departure_time,
                arrival_time=arrival_time,
                duration=duration,
                is_back_ticket=False,
                gate=self.generate_gate(),
                passenger_seat=self.generate_seat(),
                passenger_class=self.generate_class()

            )
            flight_details.append(flight)

            # Generate return flight details if applicable
            if self.back_date and (not self.no_back_ticket):
                departure_time = random.choice([10, 12, 14])
                arrival_time = random.choice([18, 20, 22])
                duration = arrival_time - departure_time

                back_flight = models.nosql.FlightDetails(
                    company=random.choice(constants.AIRLINE_COMPANIES),
                    flight_code=self.generate_flight_code(),
                    from_country=self.to_country,
                    to_country=self.from_country,
                    departure_airport=arrival_airport,
                    arrival_airport=departure_airport,
                    departure_date=self.back_date,
                    arrival_date=self.back_date,
                    departure_time=departure_time,
                    arrival_time=arrival_time,
                    duration=duration,
                    is_back_ticket=True,
                    gate=self.generate_gate(),
                    passenger_seat=self.generate_seat(),
                    passenger_class=self.generate_class()
                )
                flight_details.append(back_flight)

            # Calculate price based on number of passengers and class
            price = models.nosql.FlightPrice(value=self.calculate_ticket_price())

            status_name = random.choices(["default", "eco", "hot"], [70, 15, 15], k=1)[0]

            status_emoji = None
            status_color = None
            if status_name == "eco":
                status_emoji = "♻"
                status_color = "green"
            elif status_name == "hot":
                status_emoji = "🔥"
                status_color = "orange"

            status = models.nosql.FlightStatus(
                name=status_name,
                color=status_color,
                emoji=status_emoji
            )

            ticket = models.nosql.FlightTicket(
                price=price,
                flight_details=flight_details,
                status=status
            )

            # Add flight to available tickets
            available_tickets.append(ticket.dict())

        return available_tickets

    def calculate_ticket_price(self):
        base_price = random.randint(100, 150)  # Base price for economy class
        if self.is_business_class:
            base_price *= 2  # Double the base price for business class

        total_passengers = self.adult_passengers_count + self.teenager_passengers_count + self.child_passengers_count
        total_price = base_price * total_passengers

        return total_price