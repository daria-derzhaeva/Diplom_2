import requests
import config
from helpers import generate_random_email, generate_random_password, generate_random_name
import allure

@allure.title('Проверяем создание пользователя без обязательного поля')
def test_create_user_missing_field():
    email = generate_random_email()
    password = generate_random_password()
    name = generate_random_name()

    response_missing_email = requests.post(f'{config.REGISTRATION_URL}',
                                           json={"email": None, "password": password, "name": name})
    assert response_missing_email.status_code == 403, f"Expected 403, got {response_missing_email.status_code}"

    response_missing_password = requests.post(f'{config.REGISTRATION_URL}',
                                              json={"email": email, "password": None, "name": name})
    assert response_missing_password.status_code == 403, f"Expected 403, got {response_missing_password.status_code}"

    response_missing_name = requests.post(f'{config.REGISTRATION_URL}',
                                          json={"email": email, "password": password, "name": None})
    assert response_missing_name.status_code == 403, f"Expected 403, got {response_missing_name.status_code}"
