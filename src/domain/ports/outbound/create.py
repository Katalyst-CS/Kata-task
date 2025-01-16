from dataclasses import dataclass
from datetime import datetime

@dataclass()
class CreateResponseDTO:
    status: bool
    id: str
    title: str
    description: str
    project_id: str
    start_date: datetime
    end_date: datetime
    create_date: datetime