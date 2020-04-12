import requests,json

ENDPOINT = "http://127.0.0.1:8000/api/status"


def do(method = 'get', data={}, id=10,is_json = True):
    if is_json:
        data = json.dumps(data)
        
    r = requests.request(method,ENDPOINT+"?id="+str(id),data=data)
    print(r.text)
    return r

do(data={'id' : 12})