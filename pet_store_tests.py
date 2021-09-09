import pet_store_client
import pet_store_assert
import pet_requests
import random
import pytest
import string


pet_store_client = pet_store_client.PetStoreClient()


@pytest.fixture
def pet_name(): return ''.join([random.choice(string.ascii_lowercase) for i in range(10)])


@pytest.fixture
def pet_request_json(pet_name):
    return pet_requests.pet_json(pet_name, "available")


@pytest.fixture
def pet_response_json(pet_request_json):
    return pet_store_client.create(pet_request_json)


def test_create_pet(pet_request_json, pet_response_json):
    pet_store_assert.assert_json_data(
        expected_data=pet_request_json,
        actual_data=pet_response_json
    )


def test_get_pet(pet_request_json, pet_response_json):
    pet_get = pet_store_client.get(pet_response_json['id'])
    pet_store_assert.assert_json_data(
        expected_data=pet_response_json,
        actual_data=pet_get
    )




