import json

def is_json(json_data):
    try:
        # print(json_data)
        real_json = json.loads(json_data)
        print(real_json)
        is_valid = True
    except ValueError:
        is_valid = False

    return is_valid 