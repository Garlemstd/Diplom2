from allure import step


class OrderData:
    def __init__(self):
        self.fluorescent_bread_r2_d3 = '61c0c5a71d1f82001bdaaa6d'
        self.biocotlet_from_the_martian_magnolia = '61c0c5a71d1f82001bdaaa71'
        self.fake_ingredient_id = '1234567890abcdefghijklmn'

    @step('Модель заказа')
    def order_data(self):
        model = {
            "ingredients": [self.fluorescent_bread_r2_d3,
                            self.biocotlet_from_the_martian_magnolia,
                            self.fluorescent_bread_r2_d3]}
        return model
