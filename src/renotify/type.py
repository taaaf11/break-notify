import json
from dataclasses import asdict, dataclass


@dataclass
class Notification:
    heading: str
    body: str
    timer: int  # in minutes
    icon: str | None = None
    sound: str | None = None

    def as_json(self) -> str:
        return json.dumps(asdict(self))
