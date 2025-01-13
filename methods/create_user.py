import requests
from config import REGISTRATION_URL

class CreateUser:
    @staticmethod
    def create_user(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return requests.post(REGISTRATION_URL, json=payload)
