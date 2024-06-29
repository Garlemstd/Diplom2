import requests
import allure
from config import Config
from allure import step


class ApiClient:
    def __init__(self):
        self.url = Config().base_url

    @step('POST-запрос к серверу')
    def post(self, route=None, data=None, headers=None, params=None, json=None):
        with allure.step(f'Отправка POST-запроса на {self.url}{route}'):
            return requests.post(f'{self.url}{route}', data=data, json=json, headers=headers, params=params)

    @step('GET-запрос к серверу')
    def get(self, route=None, headers=None, params=None):
        with allure.step(f'Отправка GET-запроса на {self.url}{route}'):
            return requests.get(f'{self.url}{route}', headers=headers, params=params)

    @step('PUT-запрос к серверу')
    def put(self, route=None, data=None, headers=None, params=None, json=None):
        with allure.step(f'Отправка PUT-запроса на {self.url}{route}'):
            return requests.put(f'{self.url}{route}', data=data, headers=headers, params=params, json=json)

    @step('PATCH-запрос к серверу')
    def patch(self, route=None, headers=None, params=None, json=None):
        with allure.step(f'Отправка PATCH-запроса на {self.url}{route}'):
            return requests.patch(f'{self.url}{route}', json=json, headers=headers, params=params)

    @step('DELETE-запрос к серверу')
    def delete(self, route=None, headers=None, params=None):
        with allure.step(f'Отправка DELETE-запроса на {self.url}{route}'):
            return requests.delete(f'{self.url}{route}', headers=headers, params=params)
