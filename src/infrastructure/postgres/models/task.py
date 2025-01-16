from peewee import *
from infrastructure.postgres.connection import database

class TaskModel(Model):
    
    id = UUIDField(primary_key=True)
    title = CharField(max_length=255)
    description = TextField(null=True)
    created_date = TimestampField(null=False)
    start_date = DateField(null=True)
    end_date = DateField(null=True)
    project_id = UUIDField(null=True)

    class Meta:
        database = database
        table_name = "kATA-TBL-1000"