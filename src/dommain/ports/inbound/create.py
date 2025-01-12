from dataclasses import dataclass

@dataclass(frozen=True)
class CreateTaskDTO:
    project_id: str = ""
    title: str
    description: str = ""
    start_date: float = -1
    end_date: float = -1