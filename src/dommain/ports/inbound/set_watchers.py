from dataclasses import dataclass

@dataclass(frozen=True)
class SetWatcherDTO:
    task_id: str
    users: set 