import os

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'websale',
    user='websale',
    password='websale',
    host=os.environ.get('DB_HOST', 'localhost'),
    autorollback=True
)
