from methods.create_order import OrderMethods
import allure

@allure.title('Проверяем получение списка заказа с авторизацией')
def test_get_orders_auth_user(create_user_return_token):
    token = create_user_return_token
    get_order_methods = OrderMethods()
    response = get_order_methods.get_orders_auth_user(token)
    response_body = response.json()

    assert response.status_code == 200, f"Статус-код ответа не равен 200, пришел {response.status_code}"
    assert response_body.get("success") is True, "Поле 'success' в ответе не равно True"

@allure.title('Проверяем получение списка заказа без авторизации')
def test_get_orders_not_auth_user():
    get_order_methods = OrderMethods()
    response = get_order_methods.get_orders_not_auth_user()
    response_body = response.json()

    assert response.status_code == 401, f"Статус-код ответа не равен 401, пришел {response.status_code}"
    assert response_body.get("success") is False, "Поле 'success' в ответе не равно False"
