import allure

class TestCreateUser:
    @allure.title('Проверяем создание и удаление уникального пользователя')
    def test_create_unique_user(self, create_registered_user):
        user_data = create_registered_user['user_data']
        access_token = create_registered_user['accessToken']
        status_code = create_registered_user['status_code']

        assert status_code == 200, f"Expected status code 200 for successful registration, but got {status_code}"
        assert access_token is not None, "Expected accessToken for successful registration"
        assert user_data['email'] is not None, "Email should be present in the user data"
        assert user_data['name'] is not None, "Name should be present in the user data"