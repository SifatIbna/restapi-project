import requests

BASE_URL = " http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    for obj in data:
        print(obj['pk'])
    return data


print(get_list())