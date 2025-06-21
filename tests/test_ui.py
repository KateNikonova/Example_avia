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


@allure.epic("UI")
@allure.feature("Smoke")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(MAIN_PAGE_TITLE)
