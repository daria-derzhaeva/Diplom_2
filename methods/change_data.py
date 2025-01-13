import allure
import requests
from config import CHANGE_DATA_URL

class ChangeDate:
    @allure.step('Отправляем запрос на апдейт данных с авторизацией')
    def update_data_user_auth(self, auth_data, token):
        update_response = requests.patch(f'{CHANGE_DATA_URL}', data=auth_data,
                                         headers={'Authorization': token})
        return update_response

    @allure.step('Отправляем запрос на апдейт данных без авторизации')
    def update_data_user_not_auth(self, auth_data):
        update_response = requests.patch(f'{CHANGE_DATA_URL}', data=auth_data)
        return update_response