from abc import abstractmethod, ABC
from domain.ports.inbound import TaskRequestEvent

class Handler(ABC):

    @abstractmethod
    def handle(event: TaskRequestEvent):
        pass