from allure import step
from api_client.api_client import ApiClient
from api_client.header import Header
from steps.login_steps import LoginSteps
from data.order_data import OrderData


class OrderSteps:
    def __init__(self):
        self.api_client = ApiClient()
        self.order_route = 'api/orders'
        self.authorization = LoginSteps().user_token
        self.order_data = OrderData().order_data

    @step('Создание заказа')
    def make_an_order(self, order_data=None, token=None):
        if not order_data:
            order_data = self.order_data()
        if not token:
            token = self.authorization()
        return self.api_client.post(self.order_route, json=order_data, headers=Header(token).authorization_header())

    @step('Просмотр заказов пользователя')
    def get_user_orders(self, token=None):
        if not token:
            token = self.authorization()
        return self.api_client.get(self.order_route, headers=Header(token).authorization_header())


