import requests
from config import LOGIN_URL
import allure

@allure.title('Проверяем авторизацию с неверным логином и паролем')
def test_login_invalid_credentials():
    payload = {
        "email": "wrongemail",
        "password": "wrongpassword"
    }
    response = requests.post(LOGIN_URL, json=payload)
    assert response.status_code in [401, 404]