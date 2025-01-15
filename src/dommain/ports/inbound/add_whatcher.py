from dataclasses import dataclass

@dataclass(frozen=True)
class AddWatcherDTO:
    task_id: str
    user_id: str