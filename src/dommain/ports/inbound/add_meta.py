from dataclasses import dataclass

@dataclass(frozen=True)
class AddMetaFieldDTO:
    task_id: str
    fields: dict
