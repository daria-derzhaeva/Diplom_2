import pytest
import requests
import config
from helpers import generate_random_email, generate_random_password, generate_random_name

@pytest.fixture
def create_registered_user():
    url = f"{config.REGISTRATION_URL}"
    name = generate_random_name()
    email = generate_random_email()
    password = generate_random_password()

    user_data = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(url, json=user_data)
    response_data = response.json()
    access_token = response_data.get("accessToken")

    if not access_token:
        raise ValueError(f"User registration failed, no accessToken returned. Response: {response.text}")

    yield {
        "user_data": user_data,
        "accessToken": access_token,
        "status_code": response.status_code
    }

    delete_url = f"{config.DELETE_USER_URL}"
    headers = {"Authorization": access_token}
    requests.delete(delete_url, headers=headers)

@pytest.fixture
def login_user(create_registered_user):
    user_data = create_registered_user['user_data']
    email = user_data['email']
    password = user_data['password']

    login_url = config.LOGIN_URL
    login_payload = {
        "email": email,
        "password": password
    }
    login_response = requests.post(login_url, json=login_payload)

    print(f"Login response: {login_response.status_code}, {login_response.text}")

    assert login_response.status_code in [200, 201], f"Login failed: {login_response.text}"

    token = login_response.json().get('accessToken')
    refresh_token = login_response.json().get('refreshToken')

    return token, refresh_token, email

@pytest.fixture()
def create_user_return_token():
    random_email = generate_random_email()
    random_password = generate_random_password()
    random_name = generate_random_name()

    user_data = {
        "email": random_email,
        "password": random_password,
        "name": random_name
    }

    create_user = requests.post(f'{config.REGISTRATION_URL}', data=user_data)

    if create_user.status_code in [200, 201]:
        token = create_user.json()['accessToken']
    elif create_user.status_code == 403 and "User already exists" in create_user.text:
        login_user = requests.post(f'{config.LOGIN_URL}', data={"email": random_email, "password": random_password})
        token = login_user.json()['accessToken']
    else:
        pytest.fail(f"User creation failed with status code {create_user.status_code}: {create_user.text}")

    yield token

    requests.delete(f'{config.CHANGE_DATA_URL}', headers={'Authorization': token})