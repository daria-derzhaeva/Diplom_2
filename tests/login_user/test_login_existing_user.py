import allure

class TestLoginUser:
    @allure.title('Проверяем авторизацию под существующим пользователем')
    def test_login_existing_user(self, login_user):
        token, refresh_token, email = login_user

        assert token, "Access token is missing"
        assert refresh_token, "Refresh token is missing"
        assert email, "Email should be present"

        print(f"Logged in with token: {token}")
