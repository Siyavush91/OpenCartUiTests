import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url


    def __element(self, selector: dict, index: int):
        by = None
        if 'link_text' in selector.keys():
            by = By.LINK_TEXT
            selector = selector['link_text']
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        elif 'id' in selector.keys():
            by = By.ID
            selector = selector['id']
        return self.driver.find_elements(by, selector)[index]


    def _open(self, patch=''):
        """Открытие страницы"""
        self.driver.get(self.url + patch)


    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()


    def _clear_element_(self, selector, index=0):
        element = self.__element(selector, index)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)


    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, index=0, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index)))

    def _wait_for_alert(self):
        return EC.alert_is_present

    def _highlight(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).pause(1).perform()

    def _get_element_text(self, selector, index=0):
        return self.__element(selector, index).text

    #
    # def _upload_file(self, script, file):
    #     """Загрузка файлов в форму"""
    #
    #     dirname = os.path.dirname(__file__)
    #     filename = os.path.join(dirname, file)
    #     self.driver.execute_script(script)
    #     element = self.driver.find_element_by_css_selector("input[type=file]")
    #     element.send_keys(filename)
