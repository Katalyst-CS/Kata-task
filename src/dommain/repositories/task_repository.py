from abc import abstractmethod
from dommain.entities import TaskEntity

class TaskRepository:

    @abstractmethod
    def get_by_id(self, id: str) -> TaskEntity:
        pass

    @abstractmethod
    def create(self, entity: TaskEntity):
        pass

    @abstractmethod
    def update(self, entity: TaskEntity):
        pass

    @abstractmethod
    def add_watcher(self, task_id, user_id):
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