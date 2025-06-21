import allure
import requests
from faker import Faker


class ApiPage:
    def __init__(self, url):
        self.base_url = url
        self.fake = Faker()

    @allure.step("Отправка запроса на поиск города по коду '{term}'")
    def register_user(self, locale, term):
        """Универсальный метод для регистрации пользователя"""
        url = f"{self.base_url}/v2/code_to_places.json?"

        # Генерация данных, если они не переданы
        locale = locale or f"{self.fake.user_name()}@{self.fake.free_email_domain()}"
        term = term or self.fake.password(length=10)

        data = {
            "locale": locale,
            "term": term
        }
        return requests.get(url, data=data)
