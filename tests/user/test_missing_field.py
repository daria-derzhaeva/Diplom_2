from helpers import generate_random_email, generate_random_password, generate_random_name
from methods.create_user import CreateUser
import allure

@allure.title('Проверяем создание пользователя без обязательного поля')
def test_create_user_missing_field():
    email = generate_random_email()
    password = generate_random_password()
    name = generate_random_name()

    response_missing_email = CreateUser.create_user(None, password, name)
    assert response_missing_email.status_code == 403, f"Expected 403, got {response_missing_email.status_code}"

    response_missing_password = CreateUser.create_user(email, None, name)
    assert response_missing_password.status_code == 403, f"Expected 403, got {response_missing_password.status_code}"

    response_missing_name = CreateUser.create_user(email, password, None)
    assert response_missing_name.status_code == 403, f"Expected 403, got {response_missing_name.status_code}"
