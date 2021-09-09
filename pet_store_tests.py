import allure

import pet_store_client
import pet_store_assert
import pet_requests
import log_requests
import pytest

log_requests.debug_requests()
pet_store_client = pet_store_client.PetStoreClient()


@pytest.fixture
def pet_request_json():
    return pet_requests.pet_json(
        path_to_json='request_json/pet_request.json',
        status='available'
    )


@pytest.fixture
def pet_response_json(pet_request_json):
    return pet_store_client.create(pet_request_json)


@allure.epic("PetStore")
class TestPetStore:

    @allure.feature("POST /pet")
    def test_create_pet(self, pet_request_json, pet_response_json):
        """ обновляем id в ожидаемом json чтобы полностью сравнить запрос с ответом"""
        pet_request_json['id'] = pet_response_json['id']
        pet_store_assert.assert_json_data(
            expected_data=pet_request_json,
            actual_data=pet_response_json
        )

    @allure.feature("GET /pet")
    def test_get_pet(self, pet_request_json, pet_response_json):
        pet_get = pet_store_client.get(pet_response_json['id'])
        pet_store_assert.assert_json_data(
            expected_data=pet_response_json,
            actual_data=pet_get
        )

    @allure.feature("PUT /pet")
    def test_update_pet(self, pet_request_json, pet_response_json):
        pet_response_json['status'] = 'pending'
        pet_update = pet_store_client.update(pet_response_json)
        pet_store_assert.assert_json_data(
            expected_data=pet_response_json,
            actual_data=pet_update
        )
