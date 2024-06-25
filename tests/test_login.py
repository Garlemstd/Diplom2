import pytest
from data.user_data import UserData
import allure

@pytest.fixture(autouse=True)
def create_and_delete_user_for_login(user_steps, login_steps):
    """Эта фикстура не в conftest, т.к. она autouse - это может быть опасно, помещать ее в conftest"""
    user_steps.register_user()
    yield
    login_steps.authorization_by_user()
    user_steps.delete_user()


@pytest.fixture
def prepare_random_user():
    user = UserData().login_body().copy()
    user["email"] = 'randomemailnonexisting@mmail.ru'
    return user


class TestLogin:

    @allure.title("Авторизация от лица тестового пользователя")
    def test_user_authorization(self, login_steps):
        user_authorization = login_steps.authorization_by_user()
        assert user_authorization.ok

    @allure.title("Авторизация от лица несуществующего пользователя")
    def test_non_existing_user_authorization(self, login_steps, prepare_random_user, exceptions):
        invalid_authorization = login_steps.authorization_by_user(prepare_random_user)
        assert invalid_authorization.status_code == 401
        assert invalid_authorization.json()['message'] == exceptions.incorrect_credentials

    @allure.title("Редактирование тестового пользователя с авторизационным токеном")
    def test_edit_user_with_authorization_token(self, login_steps, user_steps):
        user_authorization = login_steps.authorization_by_user()
        assert user_authorization.ok
        update_user = user_steps.update_user(user=UserData().user_body())
        assert update_user.ok

    @allure.title("Редактирование тестового пользователя без авторизационного токена")
    def test_edit_user_without_authorization_token(self, login_steps, user_steps, exceptions):
        update_user = user_steps.update_user(token='fake_token')
        assert update_user.status_code == 401
        assert update_user.json()['message'] == exceptions.not_authorized
