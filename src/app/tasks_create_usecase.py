from domain.ports.inbound import CreateTaskDTO
from domain.repositories.task_repository import TaskRepository
from domain.entities import TaskEntity
from uuid import uuid4
from datetime import datetime

class TaskCreateUseCase:

    def __init__(self, dto: CreateTaskDTO, repository: TaskRepository):
        self.dto = dto
        self.repo = repository

    def run_case(self):
        entity = TaskEntity()
        entity.id = uuid4()
        entity.created_date = datetime.now()
        entity.title = self.dto.title
        entity.description = self.dto.description
        entity.start_date = self.dto.start_date
        entity.end_date = self.dto.end_date
        entity.project_id = self.dto.project_id
        result = self.repo.create(entity)
        return result