import os
import requests


class PetStoreClient:
    __base_url = os.environ.get('BASE_URL', -1)
    __headers = {'content-type': 'application/json', 'accept': 'application/json'}

    def __init__(self):
        if self.__base_url == -1:
            raise RuntimeError('Значение BASE_URL не задан')

    def create(self, pet_json):
        r = requests.put(f"{self.__base_url}/pet", json=pet_json, headers=self.__headers)
        return r.json()

    def update(self, pet_json):
        r = requests.put(f"{self.__base_url}/pet", json=pet_json, headers=self.__headers)
        return r.json()

    def get(self, pet_id):
        r = requests.get(f"{self.__base_url}/pet/{pet_id}", headers=self.__headers)
        return r.json()

    def delete(self, pet_id):
        r = requests.delete(f"{self.__base_url}/pet/{pet_id}", headers=self.__headers)
        return r.json()

