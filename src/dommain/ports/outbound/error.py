from dataclasses import dataclass

@dataclass
class ErrorReponseDTO:
    status: bool = False
    message: str
    code: int