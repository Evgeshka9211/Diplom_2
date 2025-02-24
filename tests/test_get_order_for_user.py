import allure
import requests

from data.request_data import Urls
from data.ingredients_data import Ingredient


@allure.suite("Получение списка заказов пользователя")
class TestGetOrderUser:

    @allure.title("Получение списка заказов пользователя. С авторизацией")
    def test_get_order_user_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        with allure.step("Отправляем запрос на получение списка заказов под авторизацией"):
            requests_create_order = requests.post(f"{Urls.MAIN_URL}{Urls.ORDER_URL}", headers=token, data=Ingredient.ingredients_data_real)
        response_get_order = requests.get(f"{Urls.MAIN_URL}{Urls.ORDER_URL}", headers=token)
        with allure.step("Запрос отправлен, проверяем результат выполнения"):
            assert response_get_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] == requests_create_order.json()['order']['number']

    @allure.title("Получение списка заказов пользователя. Без авторизации")
    def test_get_order_user_without_auth(self):
        with allure.step("Отправляем запрос на получение списка заказов без авторизации"):
            r = requests.get(f"{Urls.MAIN_URL}{Urls.ORDER_URL}")
        with allure.step("Запрос отправлен, проверяем результат выполнения"):
            assert r.status_code == 401 and r.json()['message'] == "You should be authorised"