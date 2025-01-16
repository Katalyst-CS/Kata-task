from dataclasses import dataclass
import json

@dataclass
class TaskEvent:
    type: str
    payload: any


    def to_JSON(self):
        body = {
            'type': self.type,
            'payload': self.payload
        }
        return json.dumps(body)