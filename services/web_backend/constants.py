from dataclasses import dataclass


@dataclass
class TicketStatuses:
    default = "default"
    eco = "eco"
    hot = "hot"


AIRLINE_COMPANIES = [
    "Singapore Airlines",
    "Qatar Airways",
    "Emirates",
    "Ryanair",
    "Lufthansa",
    "KLM",
    "Turkish Airlines",
    "British Airways",
    "Air France"
]

AIRPLANES = [
    "Boeing 737-800", "Boeing 767", "Airbus A320"
]

COUNTRIES = [
    {
        "country": "UAE",
        "airport": "DWC",
    },
    {
        "country": "China",
        "airport": "PEK",
    },
    {
        "country": "India",
        "airport": "DEL",
    },
    {
        "country": "USA",
        "airport": "JFK",
    },
    {
        "country": "Brazil",
        "airport": "GRU",
    },
    {
        "country": "Russia",
        "airport": "SVO",
    },
    {
        "country": "Mexico",
        "airport": "MEX",
    },
    {
        "country": "Japan",
        "airport": "NRT",
    },
    {
        "country": "Germany",
        "airport": "FRA",
    },
    {
        "country": "Turkey",
        "airport": "IST",
    },
    {
        "country": "France",
        "airport": "CDG",
    },
    {
        "country": "UK",
        "airport": "LHR",
    },
    {
        "country": "Italy",
        "airport": "FCO",
    },
    {
        "country": "South Africa",
        "airport": "JNB",
    },
    {
        "country": "South Korea",
        "airport": "ICN",
    },
    {
        "country": "Ireland",
        "airport": "DUB",
    },
]