from dataclasses import dataclass


@dataclass
class RequestData:
    url: str
    method: str
    # token: str
    params: dict | None
    json_data: dict | None
