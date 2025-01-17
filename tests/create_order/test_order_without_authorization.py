import data
from methods.create_order import OrderMethods
import allure

@allure.title('Проверяем создание заказа с ингредиентами и без авторизации')
def test_create_order_not_auth_with_ingredients():
    order_methods = OrderMethods()
    response = order_methods.create_order_not_auth(data.VALID_DATA_INGREDIENTS)
    response_body = response.json()

    assert response.status_code == 200, f"Статус-код ответа не равен 200, пришел {response.status_code}"
    assert response_body.get("success") is True, "Поле 'success' в ответе не равно True"
