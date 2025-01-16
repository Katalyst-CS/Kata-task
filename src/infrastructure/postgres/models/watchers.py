from peewee import *
from infrastructure.postgres.connection import database
from infrastructure.postgres.models import TaskModel

class WhatchersModels(Model):
    task = ForeignKeyField(TaskModel, backref='watchers', on_delete='CASCADE')  # Relación 1:N con TaskModel
    user_id = UUIDField()
    created_date = TimestampField()

    class Meta:
        database = database
        table_name = "kATA-TBL-1002"
        primary_key = CompositeKey('task','user_id')