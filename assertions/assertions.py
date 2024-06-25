from allure import step
from data.user_data import UserData


class Assertions:
    @step('Проверка равенства ID при создании заказа и ID при запросе просмотра заказов')
    def created_id_equal_requested_id(self, id_created, id_requested):
        assert id_created.json()['order']['_id'] == id_requested.json()['orders'][0]['_id']

    @step('Проверка имени в заказе с тестовым именем')
    def check_name_in_order_with_name_in_test_data(self, name_in_order, name_in_test_data):
        """Можно искать и по времени , и по email, я выбрал просто искать по имени. Это не про упрощение,
        это про лаконичность"""
        name_in_order = name_in_order.json()['order']['owner']['name']
        assert name_in_order == name_in_test_data
