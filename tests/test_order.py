import pytest
from data.user_data import UserData
from data.order_data import OrderData
import allure


@pytest.fixture(autouse=True)
def create_and_delete_user_for_make_an_order(user_steps, login_steps):
    """Эта фикстура не в conftest, т.к. она autouse - это может быть опасно, помещать ее в conftest"""
    user_steps.register_user()
    yield
    login_steps.authorization_by_user()
    user_steps.delete_user()


@pytest.fixture
def no_ingredients_data():
    return {"ingredients": []}


@pytest.fixture
def fake_ingredient_data():
    return {"ingredients": [OrderData().fake_ingredient_id]}


class TestOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_make_an_order_with_authorization(self, order_steps, assertions):
        make_an_order = order_steps.make_an_order()
        assert make_an_order.ok
        assertions.check_name_in_order_with_name_in_test_data(make_an_order, UserData().user_body()['name'])

    @allure.title("Создание заказа без авторизации")
    def test_make_an_order_without_authorization(self, order_steps):
        make_an_order_without_token = order_steps.make_an_order(token='fake_token')
        assert make_an_order_without_token.status_code == 200
        assert make_an_order_without_token.json()['success'] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_make_an_order_with_ingredients(self, order_steps):
        make_an_order_with_ingredients = order_steps.make_an_order()
        assert make_an_order_with_ingredients.ok

    @allure.title("Создание заказа без ингредиентов")
    def test_make_an_order_without_ingredients(self, order_steps, no_ingredients_data, exceptions):
        make_an_order_without_ingredients = order_steps.make_an_order(order_data=no_ingredients_data)
        assert make_an_order_without_ingredients.status_code == 400
        assert make_an_order_without_ingredients.json()['message'] == exceptions.no_ingredients_order

    @allure.title("Создание заказа с несуществующим ID ингредиента")
    def test_make_an_order_with_fake_ingredient_id(self, order_steps, fake_ingredient_data):
        make_an_order_with_fake_ingredient_id = order_steps.make_an_order(order_data=fake_ingredient_data)
        assert make_an_order_with_fake_ingredient_id.status_code == 500

    @allure.title("Получение собственных заказов с авторизацией")
    def test_get_user_orders_with_authorization(self, order_steps, assertions):
        make_an_order_to_check = order_steps.make_an_order()
        assert make_an_order_to_check.ok
        get_orders = order_steps.get_user_orders()
        assertions.created_id_equal_requested_id(make_an_order_to_check, get_orders)
        assert get_orders.ok

    @allure.title("Получение собственных заказов  без авторизации")
    def test_get_user_orders_without_authorization(self, order_steps, exceptions):
        get_orders_without_token = order_steps.get_user_orders(token='fake_token')
        assert get_orders_without_token.status_code == 401
        assert get_orders_without_token.json()['message'] == exceptions.not_authorized
    