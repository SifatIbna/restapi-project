import requests
import json 

BASE_URL = " http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    # print(data)
    for obj in data:
        r2 = requests.post(BASE_URL + ENDPOINT+"3/" + str(obj['pk']))
        print(r2.json())
        # return data

def create_update():
    new_data = {
        'user':1,
        "content":"Hey cool",
    }
    
    r = requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_data))

    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json)
        return r.json()
    return r.text

# print(create_update())

def do_obj_update():
    data = {
        "id":8,
         "content":"Bro Ki obostha",
    }
    r = requests.put(BASE_URL+ENDPOINT,data=json.dumps(data))

    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json)
        return r.json()
    return r.text

def do_obj_delete():
    data = {
        'id':8
    }
    r = requests.delete(BASE_URL+ENDPOINT,data = json.dumps(data))

    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json)
         return r.json()
    return r.text

# print(do_obj_update())
# do_obj_update()
print(do_obj_delete())