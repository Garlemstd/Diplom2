class Config:

    """
    Класс Config содержит конфигурационные параметры для тестового проекта.

    Attributes:
        _project_url (str): Базовый URL тестового проекта.

    Methods:
        base_url: Метод для получения базового URL.
    """

    _project_url = 'https://stellarburgers.nomoreparties.site/'

    @property
    def base_url(self):
        return self._project_url


