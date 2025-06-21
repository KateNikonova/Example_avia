import allure
from selenium.webdriver.common.by import By
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

    @allure.step("Клик по табу с текстом '{text}'")
    def click_tab_by_text(self, text):
        """
        Кликает на элемент таба по точному тексту
        :param text: Текст таба ('Отели', 'Авиабилеты' и т.д.)
        """
        locator = (By.XPATH, f"//div[@data-tab-text='true' and normalize-space()='{text}']")
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            # Прокрутка и клик с проверкой
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
            return True
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"tab_{text}_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Таб с текстом '{text}' не найден или недоступен для клика")

    @allure.step("Получение URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверка, что URL содержит текст '{expected_text}'")
    def check_url_contains(self, expected_text):
        current_url = self.get_current_url()
        return expected_text in current_url
