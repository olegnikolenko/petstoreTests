import random
import string
import requests
import pytest

base_url = 'https://petstore.swagger.io/v2'
headers = {'content-type': 'application/json', 'accept': 'application/json'}


@pytest.fixture
def pet_name(): return ''.join([random.choice(string.ascii_lowercase) for i in range(10)])


@pytest.fixture("status", params=["available", ""])
def status(): return status


@pytest.fixture
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


def test_post(pet_data):
    response = requests.post(f"{base_url}/pet", json=pet_data, headers=headers)
    assert response.status_code == 200
    print(response.content)