import allure


@allure.title('Проверяем авторизацию под существующим пользователем')
def test_login_existing_user(login_user):
    token, refresh_token, email = login_user

    assert token, "Access token is missing"
    assert refresh_token, "Refresh token is missing"

    print(f"Logged in with token: {token}")
