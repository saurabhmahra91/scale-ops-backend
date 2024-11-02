import os
from typing import Sequence
from dotenv import load_dotenv
from peewee import Model, PostgresqlDatabase


load_dotenv()

db = PostgresqlDatabase(
    os.environ["POSTGRES_DB"],
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    host=os.environ["POSTGRES_HOST"],
)


db.connect()


def initialize_database(models: Sequence[Model]) -> None:
    """Connect to the database and create the necessary tables."""
    db.create_tables(models)
