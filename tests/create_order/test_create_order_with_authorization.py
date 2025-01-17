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

        assert response.status_code == 200, "Статус код ответа не равен 200"
        assert response_body.get("success") is True, "Поле 'success' в ответе не равно True"

    @allure.title('Проверяем создание заказа без ингредиентов и с авторизацией')
    def test_create_order_auth_without_ingredients(self, create_user_return_token):
        token = create_user_return_token
        order_methods = OrderMethods()
        response = order_methods.create_order_auth(data.WITHOUT_DATA_INGREDIENTS, token)
        response_body = response.json()

        assert response.status_code == 400, f"Статус-код ответа не равен 400, пришел {response.status_code}"
        assert response_body.get("success") is False, "Поле 'success' в ответе не равно False"

    @allure.title('Проверяем создание заказа с авторизацией и с неверным хешем ингредиента')
    def test_create_order_auth_invalid_hash_ingredients(self, create_user_return_token):
        token = create_user_return_token
        order_methods = OrderMethods()
        response = order_methods.create_order_auth(data.INVALID_DATA_INGREDIENTS, token)

        assert response.status_code == 500, f"Статус-код ответа не равен 500, пришел {response.status_code}"
        assert data.EXPECTED_ERROR_TEXT in response.text, (
            f"Ожидался текст ошибки '{data.EXPECTED_ERROR_TEXT}', но в ответе '{response.text}'"
        )
