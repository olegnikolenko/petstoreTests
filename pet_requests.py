import json


def __request_data():
    file = open('pet_request.json')
    data = json.load(file)
    file.close()
    return data


def pet_json(name, status, id=0):
    d = __request_data()
    d['id'] = id
    d['name'] = name
    d['status'] = status
    return d