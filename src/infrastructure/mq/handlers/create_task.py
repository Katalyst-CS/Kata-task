from domain import Handler
from domain.ports.outbound import CreateResponseDTO, ErrorReponseDTO
from domain.repositories.task_repository import TaskRepository
from domain.ports.inbound import TaskRequestEvent, CreateTaskDTO
from app import TaskCreateUseCase

class CreateTaskHandler(Handler):
    
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def handle(self, event: TaskRequestEvent):
        body = event.payload
        dto = CreateTaskDTO(**body)
        usecase = TaskCreateUseCase(dto, self.repo)
        try:
            result = usecase.run_case()
            body = CreateResponseDTO(True, result.id, 
                                    result.title, 
                                    result.description,
                                    result.project_id, 
                                    result.start_date, 
                                    result.end_date, 
                                    result.created_date)
            return body
        except Exception as e:
            body = ErrorReponseDTO(message= e.message, code=0x1000)
            return body