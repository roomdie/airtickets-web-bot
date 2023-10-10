from aiogram import Dispatcher

from . import start
from . import payment


def setup(dp: Dispatcher):
    for module in (
            start, payment
    ):
        module.setup(dp)
