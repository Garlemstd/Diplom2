from api_client.api_client import ApiClient
from data.user_data import UserData
from allure import step


class LoginSteps:
    def __init__(self):
        self.api_client = ApiClient()
        self.route_login = 'api/auth/login'
        self.test_data = UserData()

    @step('Авторизация от лица пользователя')
    def authorization_by_user(self, user=None):
        if user is None:
            user = self.test_data.login_body()
        return self.api_client.post(self.route_login, user)

    @step('Извлечение токена из ответа сервера')
    def user_token(self):
        return self.authorization_by_user().json()['accessToken']

