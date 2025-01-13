from helpers import generate_random_email, generate_random_password, generate_random_name
from methods.create_user import CreateUser
import allure

@allure.title('Проверяем создание уникального пользователя')
def test_create_unique_user():
    email = generate_random_email()
    password = generate_random_password()
    name = generate_random_name()

    response = CreateUser.create_user(email, password, name)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_data = response.json()
    assert response_data.get("success") is True, "User creation was not successful"
