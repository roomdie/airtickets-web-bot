from environs import Env
import os

env = Env()
env.read_env()

DIRNAME = os.path.dirname(__file__)
os.chdir(f"{DIRNAME}//..")

BOT_TOKEN = env.str("BOT_TOKEN")
BOT_ADMINS = env.list("BOT_ADMINS")

APP_URL= env.str("APP_URL")

PSQL_HOSTNAME = env.str("PSQL_HOSTNAME")
PSQL_PORT = env.str("PSQL_PORT")
PSQL_USERNAME = env.str("PSQL_USERNAME")
PSQL_PASSWORD = env.str("PSQL_PASSWORD")
PSQL_DB_NAME = env.str("PSQL_DB_NAME")
