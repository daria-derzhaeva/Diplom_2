import allure
import pytest
import data
from methods.change_data import ChangeDate

@allure.title('Проверяем обновление данных неавторизованного пользователя')
@pytest.mark.parametrize('auth_data', data.UPDATE_DATA_USER_NOT_AUTH)
def test_update_user_not_auth(auth_data):
    user_methods = ChangeDate()
    response = user_methods.update_data_user_not_auth(auth_data)
    response_body = response.json()

    assert (response.status_code == 401 and response_body.get("success") is False)
