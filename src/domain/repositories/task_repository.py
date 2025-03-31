from abc import abstractmethod
from domain.entities import TaskEntity

class TaskRepository:

    @abstractmethod
    def get_by_id(self, id: str) -> TaskEntity:
        pass

    @abstractmethod
    def create(self, entity: TaskEntity) -> TaskEntity:
        pass

    @abstractmethod
    def update(self, entity: TaskEntity):
        pass

    @abstractmethod
    def add_watcher(self, task_id, user_id) -> bool:
        pass

    @abstractmethod
    def list_watchers(self, task_id):
        pass

    @abstractmethod
    def set_watcher(self, task_id, users):
        pass

    @abstractmethod
    def add_field(self, task_id, key, value):
        pass

    @abstractmethod
    def remove_watcher(self, task_id, user_id):
        pass

    @abstractmethod
    def remove_field(self, task_id, field_id):
        pass

    @abstractmethod
    def update_field(self, field_id, value):
        pass