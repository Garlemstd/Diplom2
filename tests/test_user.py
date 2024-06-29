import allure
from data.user_data import UserData


class TestUser:

    @allure.title("Регистрация пользователя")
    def test_register_user(self, user_steps, delete_user_after_run_test):
        create_user = user_steps.register_user()
        assert create_user.ok

    @allure.title("Регистрация уже зарегистрированного пользователя")
    def test_register_existing_user(self, user_steps, delete_user_after_run_test, exceptions):
        create_user = user_steps.register_user()
        assert create_user.ok
        create_user_duplicate = user_steps.register_user()
        assert create_user_duplicate.status_code == 403
        assert create_user_duplicate.json()['message'] == exceptions.user_duplicate

    @allure.title("Регистрация некорректного пользователя (без почты)")
    def test_register_invalid_user(self, user_steps, exceptions):
        create_user_without_email = user_steps.register_user(user=UserData().invalid_user_body())
        assert create_user_without_email.status_code == 403
        assert create_user_without_email.json()['message'] == exceptions.no_required_field
