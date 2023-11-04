import typing
import config
from flask import Flask, jsonify, request
from aiogram import Bot, types
from generator import FlightGenerator
from sqlalchemy import select

import models, database
import validator

app = Flask(__name__)
db = database.implement.PostgreSQL(
    database_name=config.PSQL_DB_NAME,
    username=config.PSQL_USERNAME,
    password=config.PSQL_PASSWORD,
    hostname=config.PSQL_HOSTNAME,
    port=5432
)

session = database.manager.create_session(db)


@app.post("/api/createInvoiceLink")
async def create_invoice_link_handle():
    flight_details = request.json["flight_details"][0]
    flight_code = flight_details["flight_code"]
    from_country = flight_details["from_country"]
    to_country = flight_details["to_country"]

    departure_time = flight_details["departure_time"]
    arrival_time = flight_details["arrival_time"]

    ticket_price = int(request.json["price"]["value"] * 100)
    ticket_currency = request.json["price"]["currency"]
    percentage = 7.4
    tax_amount = ((percentage / 100) * request.json["price"]["value"])
    tax_amount = int(tax_amount * 100)

    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    invoice_link = await bot.create_invoice_link(
        title=f"Flight {flight_code}",
        description=f"{from_country} - {to_country} / {departure_time}:00 - {arrival_time}:00",
        payload=flight_code,
        provider_token="284685063:TEST:YmRmZGFiMjdiOWQ5",
        need_name=True,
        currency=ticket_currency,
        prices=[types.LabeledPrice("Ticket", ticket_price), types.LabeledPrice("Tax", tax_amount)],
    )
    await bot.close()

    return jsonify(dict(invoice_link=invoice_link))


@app.post("/api/checkInitData")
async def check_init_data():
    data = request.json
    data = validator.safe_parse_webapp_init_data(config.BOT_TOKEN, data["_auth"])
    return data.as_json()


@app.post("/api/getPurchasedTickets")
async def get_purchased_tickets():
    user_id = request.json["user_id"]
    with session() as open_session:
        response = open_session.execute(select(
            models.sql.PurchasedTicket).filter_by(user_id=user_id))
        purchased_tickets: typing.List[models.sql.PurchasedTicket] = response.scalars().all()

    json_serialized = []
    for t in purchased_tickets:
        json_serialized.append(
            dict(
                user_id=t.user_id,
                passenger_name=t.passenger_name,
                flight_code=t.flight_code,
                details=t.details,
            )
        )
    return jsonify(json_serialized)


@app.post("/api/getSearchedFlights")
async def handle_searched_flights():

    data = models.nosql.InputFlightData(**request.json)
    generator = FlightGenerator(
        from_country=data.from_country,
        to_country=data.to_country,
        adult_passengers_count=data.adult_passengers_count,
        teenager_passengers_count=data.teenager_passengers_count,
        child_passengers_count=data.child_passengers_count,
        is_business_class=data.is_business_class,
        departure_date=data.departure_date,
        back_date=data.back_date,
        no_back_ticket=data.no_back_ticket
    )
    flights: typing.List[dict] = generator.generate_flights()

    with session() as open_session:
        for flight in flights:
            response = open_session.execute(select(models.sql.Flight))
            flight_model: models.sql.Flight = response.scalars().first()

            if flight_model:
                if flight_model.code == flight["flight_details"][0]["flight_code"]:
                    continue

            new_flight = models.sql.Flight(
                code=flight["flight_details"][0]["flight_code"],
                details=flight["flight_details"][0]
            )

            open_session.merge(new_flight)
            open_session.commit()

    return jsonify(flights)

app.run("localhost")