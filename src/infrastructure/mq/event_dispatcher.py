from domain.ports.inbound import TaskRequestEvent
from infrastructure.mq.types import *

class EventDispatcher:

    def dispatch(event: TaskRequestEvent):
        match event.type:
            case CREATE_CUSTOM_FIELD:
                pass
            case UPDATE_CUSTOM_FIELD:
                pass
            case UPDATE_TASK:
                pass

        