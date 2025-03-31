from infrastructure.postgres import connection
from infrastructure.postgres.models import CustomTaskField, TaskModel, WhatchersModels
from core.watchers_usecases import WatcherUseCases
from infrastructure.postgres.respositories import PostgrestTaskRepository
from uuid import UUID

with connection.database as db:
    db.create_tables([CustomTaskField, TaskModel, WhatchersModels])

print("Use Case")
task_repo = PostgrestTaskRepository()
watcher_usecase = WatcherUseCases(task_repo)
print(watcher_usecase.list_watchers('87f60264-3e67-40ed-822d-af4b8d3089e3'))
# print(task_repo.list_watchers('87f60264-3e67-40ed-822d-af4b8d3089e3'))
