import requests


def request(url: str, apitoken: str, method: str = "GET", body=...):
    if body is ...:
        body = {}
    headers = {
        "Accept": "application/json",
        "authorization": "Bearer " + apitoken
    }

    url = "https://api.clashofclans.com/v1" + url

    if method == "GET":
        response = requests.get(url=url, headers=headers, json=body)
    elif method == "POST":
        response = requests.post(url=url, headers=headers, json=body)
    elif method == "PUT":
        response = requests.put(url=url, headers=headers, json=body)
    else:
        return f"Invalid request method: {method}. Only GET, POST and PUT are allowed"

    response_json = response.json()

    code = get_code(response)
    return code, response, response_json


def get_code(response):
    _, response = str(response).split("[")
    response, _ = str(response).split("]")
    return int(response)


def remove_hashtag(tag):
    if tag[0] == "#":
        tag = tag.replace("#", "")
    return tag


def add_kwargs(url: str, **kwargs):
    url += "?"
    for arg in kwargs:
        url += arg
        url += "="
        url += str(kwargs[arg])
        url += "&"
    url = url[0:-1]
    return url
