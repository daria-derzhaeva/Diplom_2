import data
import allure
from methods.create_order import OrderMethods

class TestOrder:
    @allure.title('Проверяем создание заказа с ингредиентами и с авторизацией')
    def test_create_order_auth_with_ingredients(self, create_user_return_token):
        token = create_user_return_token
        order_methods = OrderMethods()
        response = order_methods.create_order_auth(data.VALID_DATA_INGREDIENTS, token)
        response_body = response.json()

        assert (
                response.status_code == 200 and
                response_body.get("success") is True)

    @allure.title('Проверяем создание заказа без ингредиентов и с авторизацией')
    def test_create_order_auth_without_ingredients(self, create_user_return_token):
        token = create_user_return_token
        order_methods = OrderMethods()
        response = order_methods.create_order_auth(data.WITHOUT_DATA_INGREDIENTS, token)
        response_body = response.json()

        assert (
                response.status_code == 400 and
                response_body.get("success") is False)

    @allure.title('Проверяем создание заказа с авторизацией и с неверным хешем ингредиента')
    def test_create_order_auth_invalid_hash_ingredients(self, create_user_return_token):
        token = create_user_return_token
        order_methods = OrderMethods()
        response = order_methods.create_order_auth(data.INVALID_DATA_INGREDIENTS, token)
        assert (response.status_code == 500)