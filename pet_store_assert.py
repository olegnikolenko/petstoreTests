

def assert_json_data(actual_data, expected_data):
    """ обновляем id в ожидаемом json чтобы полностью сравнить запрос с ответом"""
    expected_data['id'] = actual_data['id']
    assert actual_data == expected_data