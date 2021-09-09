import os
import requests


class PetStoreClient:
    __base_url = os.environ.get('BASE_URL', -1)
    __headers = {'content-type': 'application/json', 'accept': 'application/json'}

    def __init__(self):
        if self.__base_url == -1:
            raise RuntimeError('Значение BASE_URL не задан')

    def create(self, pet_json):
        return requests.put(f"{self.__base_url}/pet", json=pet_json, headers=self.__headers)

    def update(self, pet_json):
        return requests.put(f"{self.__base_url}/pet", json=pet_json, headers=self.__headers)

    def get(self, pet_id):
        return requests.get(f"{self.__base_url}/pet/{pet_id}", headers=self.__headers)

    def delete(self, pet_id):
        return requests.delete(f"{self.__base_url}/pet/{pet_id}", headers=self.__headers)

