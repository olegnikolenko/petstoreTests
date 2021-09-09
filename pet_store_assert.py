import allure


@allure.step
def assert_json_data(actual_data, expected_data):
    assert actual_data == expected_data