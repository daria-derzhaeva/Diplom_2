import allure
import pytest
import data
from methods.change_data import ChangeDate

@allure.title('Проверяем обновление данных пользователя')
@pytest.mark.parametrize('auth_data', data.UPDATE_DATA_USER_AUTH)
def test_update_user_auth(auth_data, create_user_return_token):
    token = create_user_return_token
    user_methods = ChangeDate()
    response = user_methods.update_data_user_auth(auth_data, token)
    response_body = response.json()

    assert (response.status_code == 200 and response_body.get("success") is True)
