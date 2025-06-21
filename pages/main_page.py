import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.maximize_window()

    def _wait_for_elements(self, locator, multiple=False, timeout=10):
        if multiple:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
        else:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))

    @allure.step("Проверка заголовка страницы")
    def check_page_title(self, expected_title):
        WebDriverWait(self.driver, 10).until(EC.title_is(expected_title))
        return True
