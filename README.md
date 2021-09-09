export BASE_URL=https://petstore.swagger.io/v2

pytest -c pytest.ini --clean-alluredir --alluredir=./tmp/my_allure_results ./*_tests.py

allure serve ./tmp/my_allure_results
