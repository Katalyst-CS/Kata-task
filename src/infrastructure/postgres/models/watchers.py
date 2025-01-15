from peewee import *
from infrastructure.postgres.connection import database

class WhatchersModels(Model):
    task_id = UUIDField(primary_key=True)
    user_id = UUIDField(primary_key=True)
    created_date = TimestampField()

    class Meta:
        database = database