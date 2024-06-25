from allure import step


class UserData:

    @staticmethod
    @step('Модель пользователя для регистрации')
    def user_body():
        model = {
            "email": "random-email-test@mail.ru",
            "password": "some_p@ss0rd-123",
            "name": "Yuri Gagarin"}
        return model

    @staticmethod
    @step('Модель пользователя для авторизации')
    def login_body():
        model = {
            "email": "random-email-test@mail.ru",
            "password": "some_p@ss0rd-123"
        }
        return model

    @step('Модель пользователя без почты')
    def invalid_user_body(self):
        valid_user = self.user_body().copy()
        valid_user.pop("email")
        return valid_user

