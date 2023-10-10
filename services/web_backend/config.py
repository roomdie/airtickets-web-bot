import os
from environs import Env
from services import database

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

DIRNAME = os.path.dirname(__file__)
os.chdir(f"{DIRNAME}//..")

PSQL_HOSTNAME = env.str("PSQL_HOSTNAME")
PSQL_PORT = env.str("PSQL_PORT")
PSQL_USERNAME = env.str("PSQL_USERNAME")
PSQL_PASSWORD = env.str("PSQL_PASSWORD")
PSQL_DB_NAME = env.str("PSQL_DB_NAME")

db = database.implement.PostgreSQL(
    database_name=PSQL_DB_NAME,
    username=PSQL_USERNAME,
    password=PSQL_PASSWORD,
    hostname=PSQL_HOSTNAME,
    port=5432
)

session = database.manager.create_session(db)
