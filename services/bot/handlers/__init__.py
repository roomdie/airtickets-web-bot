from . import users
from . import groups
from . import admins

from aiogram import Dispatcher


def setup(dp: Dispatcher):
    for module in (users,):
        module.setup(dp)
