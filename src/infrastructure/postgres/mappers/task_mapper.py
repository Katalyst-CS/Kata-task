from dommain.entities import TaskEntity
from infrastructure.postgres.models import TaskModel

class TaskMapper:

    def domain2model(self, entity: TaskEntity) -> TaskModel:
        model = TaskModel()
        model.description = entity.description
        model.created_date = entity.created_date
        model.end_date = entity.end_date
        model.start_date = entity.start_date
        model.id = entity.id
        model.project_id = entity.project_id
        model.title = entity.title
        return model
    
    def model2domain(self, model: TaskModel) -> TaskEntity:
        entity = TaskEntity()
        entity.id = model.id
        entity.title = model.title
        entity.description = model.description
        entity.created_date = model.created_date
        entity.project_id = model.project_id
        entity.start_date = model.start_date
        entity.end_date = model.end_date
        return entity