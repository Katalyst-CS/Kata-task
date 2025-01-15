from peewee import *
from infrastructure.postgres.connection import database

class CustomTaskField(Model):
    id = UUIDField(null=False, primary_key=True)
    key = CharField(max_length=300, null=False)
    value = TextField(null=True)
    task_id = UUIDField(null=False)
    created_date = TimestampField()
    modified_date = TimestampField()

    class Meta:
        database = database