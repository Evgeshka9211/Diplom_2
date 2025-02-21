import allure
import requests

from data.request_data import Urls
from data.user_data import User

@allure.suite('Редактирование пользователя')
class TestChangingUserData:

    @allure.title("Успешное изменение значения email зарегистрированного пользователя")
    def test_edit_user_email_with_auth(self, create_user):
        payload = {'email': User.create_data_user()["email"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Urls.USER_URL}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == payload["email"]

    @allure.title("Успешное изменение значения password зарегистрированного пользователя")
    def test_edit_user_password_with_auth(self, create_user):
        payload = {'password': User.create_data_user()["password"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Urls.USER_URL}", headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Успешное изменение значения name авторизованного пользователя")
    def test_edit_user_name_with_auth(self, create_user):
        payload = {'name': User.create_data_user()["name"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Urls.USER_URL}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['name'] == payload["name"]

    @allure.title("Изменение данных пользователя без авторизации")
    def test_edit_user_data_not_auth(self):
        r = requests.patch(f"{Urls.MAIN_URL}{Urls.USER_URL}", data=User.create_data_user())
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'
