import requests


def request(url, apitoken):# get
    headers = {
        "Accept": "application/json",
        "authorization": "Bearer " + apitoken
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()
    return response_json, response


def requestpost(url, apitoken, body):# post
    headers = {
        "Accept": "application/json",
        "authorization": "Bearer " + apitoken,
    }

    json = {
        "token": body
    }

    response = requests.post(url, headers=headers, json=json)
    response_json = response.json()
    return response_json, response


def rm_hashtag(tag):
    if tag[0:1] == "#":
        tag = tag.replace("#", "")
    return tag


def awnsers(response, response_json):
    if str(response) == "<Response [200]>":
        answer = "Successful response"
        code = 200
    elif str(response) == "<Response [400]>":
        answer = "Client provided incorrect parameters for the request"
        code = 400
    elif str(response) == "<Response [403]>":
        answer = "Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource"
        code = 403
    elif str(response) == "<Response [404]>":
        answer = "Resource was not found"
        code = 404
    elif str(response) == "<Response [429]>":
        answer = "Request was throttled, because amount of requests was above the threshold defined for the used API token"
        code = 429
    elif str(response) == "<Response [500]>":
        answer = "Unknown error happened when handling the request"
        code = 500
    elif str(response) == "<Response [503]>":
        answer = "Service is temprorarily unavailable because of maintenance"
        code = 503

    return code, answer, response_json