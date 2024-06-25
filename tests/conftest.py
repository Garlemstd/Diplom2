import pytest
from allure import step
from steps.user_steps import UserSteps
from steps.login_steps import LoginSteps
from steps.order_steps import OrderSteps
from api_client.api_client import ApiClient
from server_exceptions.exceptions_text import ExceptionsText
from assertions.assertions import Assertions


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
