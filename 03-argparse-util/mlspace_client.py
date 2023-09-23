from mlspace_request import RequestData


def get_token():
    return "my-token"


def get_headers(method: str):
    headers = {"Authorization": f"Bearer {get_token()}"}
    headers["method"] = "test"
    return headers


def request(reqest_data: RequestData):
    headers = get_headers(reqest_data.method)

    print(f"request data : {reqest_data}, headers = {headers}")
    # execute rest api call
