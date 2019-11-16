from page_object import AdminLogin
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert


def test_login(browser, url, simple_logger):
    """Тест на авторизацию в админке"""
    AdminLogin(browser, url)\
        .open() \
        .input_username("admin") \
        .input_password("25191") \
        .submit_login()
    simple_logger.error("test failed")
    simple_logger.debug("test auth failed")
    (Alert(browser).accept())
