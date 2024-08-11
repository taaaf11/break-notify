import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Notification:
    heading: str
    body: str
    timer: int  # in minutes
    icon: str | None = None

    def as_json(self) -> str:
        return json.dumps(asdict(self))
