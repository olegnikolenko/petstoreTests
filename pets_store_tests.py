import random
import string
import requests
import pytest
import log_requests

log_requests.debug_requests()
base_url = 'https://petstore.swagger.io/v2'
headers = {'content-type': 'application/json', 'accept': 'application/json'}


@pytest.fixture
def pet_name(): return ''.join([random.choice(string.ascii_lowercase) for i in range(10)])


@pytest.fixture(params=["available", "sold", "pending",  pytest.param("", marks=pytest.mark.xfail)])
def status(request): return request.param


def pet_data(pet_name, status): return {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": pet_name,
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": status
}


def create_pet(pet_name, status):
    return requests.post(f"{base_url}/pet", json=pet_data(pet_name, status), headers=headers)


def test_create_pet(pet_name, status):
    response = requests.post(f"{base_url}/pet", json=pet_data(pet_name, status), headers=headers)
    assert response.json().get("name") == pet_name and response.json().get("status") == status
    assert response.status_code == 200
    print(response.text)


def test_get_pet(pet_name):

    """ тут тест подмигивает """

    created_pet = create_pet(pet_name, "available")
    pet_id = created_pet.json().get("id")

    get_pet = requests.get(f"{base_url}/pet/{pet_id}", headers=headers)
    assert get_pet.json().get("name") == pet_name and get_pet.json().get("status") == "available"
    assert get_pet.status_code == 200


def test_get_pet_by_saved_id():

    """ не очень удачный пример с захардкоженным id"""

    pet_id = 9223372000666096368
    get_pet = requests.get(f"{base_url}/pet/{pet_id}", headers=headers)
    assert get_pet.json().get("id") == pet_id
    assert get_pet.status_code == 200
