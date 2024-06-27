import pytest
from allure import step
import allure
from steps.user_steps import UserSteps
from steps.login_steps import LoginSteps
from steps.order_steps import OrderSteps
from api_client.api_client import ApiClient
from server_exceptions.exceptions_text import ExceptionsText
from assertions.assertions import Assertions
from data.user_data import UserData
from data.order_data import OrderData


@pytest.fixture
def delete_user_after_run_test(user_steps, login_steps):
    with allure.step('Удаление пользователя после теста'):
        yield
        authorization = login_steps.authorization_by_user()
        assert authorization.ok
        delete_user = user_steps.delete_user()
        assert delete_user.ok


@pytest.fixture
def user_data():
    return UserData()


@pytest.fixture
def create_and_delete_user_for_test(user_steps, login_steps):
    user_steps.register_user()
    yield
    login_steps.authorization_by_user()
    user_steps.delete_user()


@pytest.fixture
def prepare_random_user():
    user = UserData().login_body().copy()
    user["email"] = 'randomemailnonexisting@mmail.ru'
    return user


@pytest.fixture
def no_ingredients_data():
    return {"ingredients": []}


@pytest.fixture
def fake_ingredient_data():
    return {"ingredients": [OrderData().fake_ingredient_id]}


@pytest.fixture
@step('Подготовка api-клиента')
def api_client():
    return ApiClient()


@pytest.fixture
@step('Подготовка текстов ошибок сервера')
def exceptions():
    return ExceptionsText()


@pytest.fixture
@step('Подготовка шагов пользователя')
def user_steps():
    return UserSteps()


@pytest.fixture
@step('Подготовка шагов логина')
def login_steps():
    return LoginSteps()


@pytest.fixture
@step('Подготовка шагов заказа')
def order_steps():
    return OrderSteps()


@pytest.fixture
@step('Подготовка кастомных ассертов')
def assertions():
    return Assertions()
