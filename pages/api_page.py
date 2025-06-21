import allure
import requests
from faker import Faker
from config import API_HEADERS


class ApiPage:
    def __init__(self, url):
        self.base_url = url
        self.fake = Faker()
        self.headers = API_HEADERS

    @allure.step("Отправка запроса на поиск города по коду '{term}'")
    def get_city_by_term(self, locale, term):
        """Метод для поиска города по коду аэропорта"""
        url = f"{self.base_url}/v2/code_to_places.json"

        params = {
            "locale": locale,
            "term": term
        }
        return requests.get(url, headers=self.headers, params=params)
