from domain.entities.task import TaskEntity
from domain.repositories.task_repository import TaskRepository
from infrastructure.postgres.mappers.task_mapper import TaskMapper
from infrastructure.postgres.models import WhatchersModels, TaskModel
from domain.exception import TaskNotFoundError
from datetime import datetime
from uuid import uuid4

class PostgrestTaskRepository(TaskRepository):

    def __exist_task__(self, task_id) -> bool:
        task = TaskModel.select().where(TaskModel.id == task_id).get()
        if task is None:
            raise TaskNotFoundError("La tarea no existe")
        return True

    def add_watcher(self, task_id, user_id):
        self.__exist_task__(task_id)
        watcher = WhatchersModels()
        watcher.user_id = user_id
        watcher.task_id = task_id
        watcher.created_date = datetime.now()
        watcher.save()
        return True
    
    def set_watcher(self, task_id, users):
        self.__exist_task__(task_id)
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
    
    def list_watchers(self, task_id):
        print("Checking task")
        self.__exist_task__(task_id)
        model = TaskModel.select().where(TaskModel.id == task_id).get()
        mapper = TaskMapper()
        entity = mapper.model2domain(model)
        return entity.watchers
