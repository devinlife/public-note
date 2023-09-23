import httpx
from mlspace_request import ActionType

action_map = {
    ActionType.CREATE: "post",
    ActionType.READ: "get",
    ActionType.UPDATE: "put",
    ActionType.DELETE: "delete",
    ActionType.PATCH: "patch",
}


def _get_token():
    return "my-token"


def _get_headers(action: ActionType):
    if not action:
        print(f"{action} is not valid.")

    headers = {"Authorization": f"Bearer {_get_token()}"}
    headers["method"] = "test"
    return headers


def request(request_data: dict):
    request_data["method"] = action_map.get(request_data.get("action"))

    # execute rest api call
    _reqeust(request_data)


def _reqeust(request_data):
    action = request_data.get("action")
    headers = _get_headers(request_data.get("action"))
    data = request_data.get("data")
    json = request_data.get("json")
    params = request_data.get("params")

    print(f"action = {action} headers = {headers} data = {data} json = {json}")

    match action:
        case ActionType.CREATE:
            _http_post(headers, data, json)
        case ActionType.READ:
            _http_get(headers, params)
        case _:
            print(f"Action not found: {action}")


def _http_get(url, headers=None, params=None):
    print(f"_http_get : {headers}/{params}")
    if not params:
        return None

    try:
        with httpx.Client() as client:
            response = client.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as err:
        print(f"An HTTP error occurred: {err}")
        return None


def _http_post(url, headers=None, data=None, json=None):
    print(f"_http_get : {headers}/{data}")
    if not data:
        return None

    # try:
    #     with httpx.Client() as client:
    #         response = client.post(url, data=data, json=json, headers=headers)
    #         response.raise_for_status()
    #         return response.json()
    # except httpx.HTTPError as err:
    #     print(f"An HTTP error occurred: {err}")
    #     return None
