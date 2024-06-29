import pytest
from allure import step
import allure
from steps.user_steps import UserSteps
from steps.login_steps import LoginSteps
from steps.order_steps import OrderSteps
from server_exceptions.exceptions_text import ExceptionsText
from assertions.assertions import Assertions
from data.user_data import UserData


@step('Удаление тестового пользователя после прогона тестов')
@pytest.fixture
def delete_user_after_run_test(user_steps, login_steps):
    with allure.step('Удаление пользователя после теста'):
        yield
        login_steps.authorization_by_user()
        user_steps.delete_user()


@step('Создание пользователя для теста и удаление после теста')
@pytest.fixture
def create_and_delete_user_for_test(user_steps, login_steps):
    user_steps.register_user()
    yield
    login_steps.authorization_by_user()
    user_steps.delete_user()


@step('Подготовка случайного email для теста')
@pytest.fixture
def prepare_random_user():
    user = UserData().login_body().copy()
    user["email"] = 'randomemailnonexisting@mmail.ru'
    return user


@step('Подготовка текстов ошибок сервера')
@pytest.fixture
def exceptions():
    return ExceptionsText()


@step('Подготовка шагов пользователя')
@pytest.fixture
def user_steps():
    return UserSteps()


@step('Подготовка шагов логина')
@pytest.fixture
def login_steps():
    return LoginSteps()


@step('Подготовка шагов заказа')
@pytest.fixture
def order_steps():
    return OrderSteps()


@step('Подготовка кастомных ассертов')
@pytest.fixture
def assertions():
    return Assertions()
