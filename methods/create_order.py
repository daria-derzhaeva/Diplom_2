import allure
import requests
from config import CREATE_ORDER

class OrderMethods:
    @allure.step('Отправляем запрос на создание заказа c авторизацией')
    def create_order_auth(self, order_data, token):
        create_order_auth = requests.post(f'{CREATE_ORDER}',
                                          data=order_data, headers={'Authorization': token})
        return create_order_auth

    @allure.step('Отправляем запрос на создание заказа без авторизации')
    def create_order_not_auth(self, order_data):
        create_order_auth = requests.post(f'{CREATE_ORDER}', data=order_data, )
        return create_order_auth

    @allure.step('Отправляем запрос на получение списка заказа конкретного пользователя с авторизацией')
    def get_orders_auth_user(self, token):
        get_orders = requests.get(f'{CREATE_ORDER}', headers={'Authorization': token})
        return get_orders

    @allure.step('Отправляем запрос на получение списка заказа без авторизации')
    def get_orders_not_auth_user(self):
        get_orders = requests.get(f'{CREATE_ORDER}')
        return get_orders