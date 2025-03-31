from domain.repositories.task_repository import TaskRepository
from domain.ports.inbound.add_whatcher import AddWatcherDTO

class WatcherAddUseCase:

    def __init__(self, dto: AddWatcherDTO, repo: TaskRepository):
        self.dto = dto
        self.repo = repo

    def run_case(self):
        result = self.repo.add_watcher(self.dto.task_id, self.dto.user_id)
        return result