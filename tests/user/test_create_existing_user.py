from methods.create_user import CreateUser
from helpers import generate_random_email, generate_random_password, generate_random_name
import allure

@allure.title('Проверяем создание пользователя, который уже зарегистрирован')
def test_create_existing_user():
    email = generate_random_email()
    password = generate_random_password()
    name = generate_random_name()

    first_response = CreateUser.create_user(email, password, name)
    assert first_response.status_code == 200, f"Expected 200, got {first_response.status_code}"

    second_response = CreateUser.create_user(email, password, name)
    assert second_response.status_code == 403, f"Expected 403, got {second_response.status_code}"

    response_data = second_response.json()
    assert "message" in response_data, "Response does not contain 'message'"
    assert "already exists" in response_data["message"], f"Unexpected error message: {response_data['message']}"
