import pytest
import allure
import requests

from data.request_data import Urls, Helper
from data.user_data import User

@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание нового пользователя.')
    def test_create_new_user_success(self):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.REGISTER_USER_URL}', data=User.create_data_user())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Повторное создание пользователя. Дублирование.')
    def test_create_double_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.REGISTER_USER_URL}', data=User.data_double)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.title('Создание пользователя с отсутствием обязательных полей.')
    @pytest.mark.parametrize("user_data", [User.data_empty_email, User.data_empty_password, User.data_empty_name])
    def test_create_user_incorrect_data(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.REGISTER_USER_URL}', data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text