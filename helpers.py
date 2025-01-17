import random
import string
import uuid

def generate_random_login(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_email(domain="yandex.ru"):
    unique_id = str(uuid.uuid4())[:8]
    return f"test-{unique_id}@{domain}"

def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_name(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length)).capitalize()
