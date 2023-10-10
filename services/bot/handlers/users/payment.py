from aiogram import types, Dispatcher
from sqlalchemy import select
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class PurchasedTicket(Base):
    __tablename__ = "purchased_ticket"

    index: BigInteger = Column(Integer, primary_key=True)
    user_id: BigInteger = Column(BigInteger)
    passenger_name: String = Column(String)
    flight_code: String = Column(String)
    details = Column(JSON)


class Flight(Base):
    __tablename__ = "flight"

    index: BigInteger = Column(Integer, primary_key=True)
    code: String = Column(String)
    details = Column(JSON)


async def checkout_query_handler(query: types.PreCheckoutQuery):
    try:
        await query.bot.answer_pre_checkout_query(
            query.id,
            ok=True,
        )
    except Exception as e:
        await query.bot.answer_pre_checkout_query(
            query.id,
            ok=False,
            error_message=f"Error: {e}"
        )


async def successful_payment_handler(message: types.Message):
    session = message.bot.get("session")

    passenger_name = message.successful_payment.order_info.name
    flight_code = message.successful_payment.invoice_payload
    print(flight_code)

    async with session() as open_session:
        response: Flight = await open_session.execute(select(
            Flight).filter_by(code=flight_code))
        flight = response.scalars().first()

        new_purchased_ticket = PurchasedTicket(
            user_id=message.from_user.id,
            passenger_name=passenger_name,
            details=flight.details,
            flight_code=flight_code
        )
        await open_session.merge(new_purchased_ticket)
        await open_session.commit()

    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="<b>Thank you for your purchase!</b>\n\n"
             "You can always view your purchased tickets using this link:"
             "https://t.me/AirticketsWebAppBot/tickets"
    )


def setup(dp: Dispatcher):
    dp.register_message_handler(
        successful_payment_handler,
        content_types=types.ContentTypes.SUCCESSFUL_PAYMENT,
    )

    dp.register_pre_checkout_query_handler(
        checkout_query_handler
    )
