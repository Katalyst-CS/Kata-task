from dataclasses import dataclass

@dataclass(frozen=True)
class TaskRequestEvent:
    type: str
    payload: any