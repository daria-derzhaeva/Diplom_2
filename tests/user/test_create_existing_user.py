import requests
import allure
from helpers import generate_random_email, generate_random_password, generate_random_name
import config

@allure.title('Проверяем создание пользователя, который уже зарегистрирован')
def test_create_existing_user():
    email = generate_random_email()
    password = generate_random_password()
    name = generate_random_name()

    user_data = {
        "email": email,
        "password": password,
        "name": name
    }

    first_response = requests.post(f'{config.REGISTRATION_URL}', json=user_data)
    assert first_response.status_code == 200, f"Expected 200, got {first_response.status_code}"  # Ожидаем 202 вместо 200

    second_response = requests.post(f'{config.REGISTRATION_URL}', json=user_data)
    assert second_response.status_code == 403, f"Expected 403, got {second_response.status_code}"

    response_data = second_response.json()
    assert "message" in response_data, "Response does not contain 'message'"
    assert "already exists" in response_data["message"], f"Unexpected error message: {response_data['message']}"

    delete_url = f"{config.DELETE_USER_URL}"
    headers = {"Authorization": first_response.json().get('accessToken')}
    delete_response = requests.delete(delete_url, headers=headers)
    assert delete_response.status_code == 202, f"Failed to delete user: {delete_response.status_code}"  # Ожидаем 202 вместо 200
