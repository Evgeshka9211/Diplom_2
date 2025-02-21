import allure
import requests

from data.request_data import Urls
from data.user_data import User

@allure.suite('Авторизация пользователя')
class TestUserLogin:

    @allure.title('Авторизация пользователя. Корректные учетные данные')
    def test_login_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.LOGIN_USER_URL}', data=User.data_real)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.title('Авторизация пользователя. Некорректные учетные данные')
    def test_login_user_error(self):

        response = requests.post(f'{Urls.MAIN_URL}{Urls.LOGIN_USER_URL}', data=User.data_fake)
        assert response.status_code == 401 and response.json().get('success') == False
