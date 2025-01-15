from dommain.entities.task import TaskEntity
from dommain.repositories.task_repository import TaskRepository
from infrastructure.postgres.mappers.task_mapper import TaskMapper
from infrastructure.postgres.models import WhatchersModels, TaskModel
from dommain.exception import TaskNotFoundError
from datetime import datetime
from uuid import uuid4

class PostgrestTaskRepository(TaskRepository):

    def add_watcher(self, task_id, user_id):
        task = TaskModel.select().where(TaskModel.id == task_id).get()
        if task is None:
            raise TaskNotFoundError("La tarea no existe")
        watcher = WhatchersModels()
        watcher.user_id = user_id
        watcher.task_id = task_id
        watcher.created_date = datetime.now()
        watcher.save()
        return True
    
    def set_watcher(self, task_id, users):
        task = TaskModel.select().where(TaskModel.id == task_id).get()
        if task is None:
            raise TaskNotFoundError("La tarea no existe")
        for user in users:
            watcher = WhatchersModels()
            watcher.user_id = user
            watcher.task_id = task_id
            watcher.created_date = datetime.now()
            watcher.save()
        return True
    
    def create(self, entity: TaskEntity):
        mapper = TaskMapper()
        model = mapper.domain2model(entity)
        if model.id is None:
            model.id = uuid4()
        return model.save() == 1
    
    def get_by_id(self, id) -> TaskEntity:
        model = TaskModel.select().where(TaskModel.id == id).get()
        mapper = TaskMapper()
        entity = mapper.model2domain(model)
        return entity
