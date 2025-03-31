from domain.repositories.task_repository import TaskRepository


class WatcherUseCases:

    def __init__(self, repository: TaskRepository):
        self.repository = repository
    
    def list_watchers(self, task_id):
        print("list watchers")
        result = self.repository.list_watchers(task_id)
        return result
    
    def add_watcher(self, tasak_id, user_id):
        result = self.repository.add_watcher(tasak_id, user_id)
        return result