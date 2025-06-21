import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from config import MAIN_URL, MAIN_PAGE_TITLE


@pytest.fixture
def main_page():
    driver = webdriver.Chrome()
    page = MainPage(driver, MAIN_URL)
    yield page
    driver.quit()


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(MAIN_PAGE_TITLE)


@allure.feature("Navigation")
@allure.story("UI")
@pytest.mark.ui
@pytest.mark.parametrize("button_text, url_part", [
    ("Отели", "hotels"),
    ("Короче", "guides"),
])
def test_navigation(main_page, button_text, url_part):
    with allure.step(f"Клик по кнопке '{button_text}'"):
        main_page.click_tab_by_text(button_text)

    with allure.step(f"Проверка, что URL содержит '{url_part}'"):
        assert main_page.check_url_contains(url_part)
