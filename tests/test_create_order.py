import allure
import requests

from data.request_data import Urls, Helper
from data.ingredients_data import Ingredient

@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        r = requests.post(f"{Urls.MAIN_URL}{Urls.ORDER_URL}", headers=token, data=Ingredient.ingredients_data_real)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Создание заказа не авторизованным пользователем")
    def test_create_order_without_auth(self):
        r = requests.post(f"{Urls.MAIN_URL}{Urls.ORDER_URL}", data=Ingredient.ingredients_data_real)
        assert r.status_code == 200 and r.json().get("success") is True


    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredient(self):
        r = requests.post(f"{Urls.MAIN_URL}{Urls.ORDER_URL}")
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"

    @allure.title("Создание с невалидным хешем ингредиента")
    def test_create_order_with_ingredient_fake_hash(self):
        response = requests.post(Urls.MAIN_URL + Urls.ORDER_URL, headers= Helper.headers, json=Ingredient.ingredients_data_fake)
        assert response.status_code == 500 and 'Internal Server Error' in response.text