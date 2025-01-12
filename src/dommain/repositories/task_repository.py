from abc import abstractmethod
from dommain.entities import TaskEntity

class TaskRepository:

    @abstractmethod
    def get_by_id(self, id: str):
        pass

    @abstractmethod
    def update(self, entity: TaskEntity):
        pass