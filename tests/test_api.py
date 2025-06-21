import pytest
import allure
from pages.api_page import ApiPage


@pytest.fixture
def api_page():
    return ApiPage()


@allure.feature("Поиск города")
@allure.story("API")
@allure.title("поиск города по коду '{term}'")
@pytest.mark.positive
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.parametrize
def test_register_with_ru_email(api_page):
    with allure.step("Отправляем запрос на регистрацию с email  в домене ru"):
        response = api_page.register_user(email=f"test_{api_page.fake.user_name()}@ya.ru")
    with allure.step("Проверяем статус-код"):
        assert response.status_code == 201, "Ожидается статус код 201"
