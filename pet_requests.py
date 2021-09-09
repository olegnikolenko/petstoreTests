import json
import random
import string
import allure


def __request_data(path_to_json):
    file = open(path_to_json)
    data = json.load(file)
    file.close()
    return data


@allure.step
def pet_json(path_to_json, status, id=0):
    d = __request_data(path_to_json)
    d['id'] = id
    d['name'] = ''.join([random.choice(string.ascii_lowercase) for i in range(10)])
    d['status'] = status
    return d