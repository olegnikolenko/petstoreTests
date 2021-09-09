import pet_store_client
import pet_requests
import random
import pytest
import string


client = pet_store_client.PetStoreClient()


@pytest.fixture
def pet_name(): return ''.join([random.choice(string.ascii_lowercase) for i in range(10)])


@pytest.fixture
def pet_(): return ''.join([random.choice(string.ascii_lowercase) for i in range(10)])


def test_create_pet(): return