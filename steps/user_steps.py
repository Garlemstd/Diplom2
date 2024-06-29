from api_client.api_client import ApiClient
from data.user_data import UserData
from steps.login_steps import LoginSteps
from allure import step
from api_client.header import Header


class UserSteps:
    def __init__(self):
        self.api_client = ApiClient()
        self.route_register = 'api/auth/register'
        self.route_user = 'api/auth/user'
        self.test_data = UserData()
        self.authorization = LoginSteps().authorization_by_user

    @step('Запрос токена у сервера')
    def get_token(self):
        return self.authorization().json()["accessToken"]

    @step('Регистрация пользователя')
    def register_user(self, user=None):
        if not user:
            user = self.test_data.user_body()
        return self.api_client.post(self.route_register, json=user)

    @step('Удаление пользователя')
    def delete_user(self, token=None):
        if not token:
            token = self.get_token()
        return self.api_client.delete(self.route_user, headers=Header(token).authorization_header())

    @step('Обновление данных пользователя')
    def update_user(self, user=None, token=None):
        if not user:
            user = self.test_data.user_body()
        if not token:
            token = self.get_token()
        return self.api_client.patch(self.route_user, json=user, headers=Header(token).authorization_header())

