import pytest
import requests
import config
import data
from helpers import generate_random_email, generate_random_password, generate_random_name
from methods.create_user import CreateUser

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


@pytest.fixture()
def create_user():
    response = requests.post(f'{config.REGISTRATION_URL}', json=data.DATA_USER)

    if response.status_code not in [200, 201]:
        pytest.fail(f"User creation failed: {response.status_code} - {response.text}")

    token = response.json().get('accessToken')
    if not token:
        pytest.fail(f"'accessToken' not found in response: {response.json()}")

    yield response
    requests.delete(f'{config.CHANGE_DATA_URL}', headers={'Authorization': token})

@pytest.fixture
def login_user():
    email = generate_random_email()
    password = generate_random_password()
    name = generate_random_name()

    create_response = CreateUser.create_user(email, password, name)

    print(f"Create user response: {create_response.status_code}, {create_response.text}")

    assert create_response.status_code in [200, 201], f"User creation failed: {create_response.text}"

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
