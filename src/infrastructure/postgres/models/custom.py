from peewee import *
from infrastructure.postgres.models import TaskModel
from infrastructure.postgres.connection import database

class CustomTaskField(Model):
    id = UUIDField(null=False, primary_key=True)
    key = CharField(max_length=300, null=False)
    value = TextField(null=True)
    task = ForeignKeyField(TaskModel, backref='custom_fields', on_delete='CASCADE')  # 'task' es el nombre del campo en esta tabla
    created_date = TimestampField()
    modified_date = TimestampField()

    class Meta:
        database = database
        table_name = "kATA-TBL-1001"