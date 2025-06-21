import pytest
import allure
from pages.api_page import ApiPage
from config import API_SUGGESTED_URL


@pytest.fixture
def api_suggested_page():
    return ApiPage(API_SUGGESTED_URL)


@allure.epic("API")
@allure.feature("Поиск города")
@allure.title("поиск города по коду '{term}'")
@pytest.mark.positive
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.parametrize("locale, term, name", [
    ("ru_RU", "KUF", "Самара"),
    ("ru_RU", "LED", "Санкт-Петербург"),
    ("en_EN", "BUE", "Buenos Aires"),
])
def test_register_with_ru_email(api_suggested_page, locale, term, name):
    with allure.step("Отправляем запрос на регистрацию с email  в домене ru"):
        response = api_suggested_page.get_city_by_term(locale, term)
    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200, "Ожидается статус код 200"
        print(response)
    with allure.step("Проверяем название города"):
        assert response.json()[0]["name"] == name, \
            f"Ожидается название города '{name}'"
