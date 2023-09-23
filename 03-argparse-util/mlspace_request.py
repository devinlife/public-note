from dataclasses import dataclass
from enum import Enum, auto


class ActionType(Enum):
    CREATE = auto()
    READ = auto()
    UPDATE = auto()
    DELETE = auto()
    PATCH = auto()


@dataclass
class RequestData:
    url: str
    action: ActionType
    params: dict | None
    json: dict | None
