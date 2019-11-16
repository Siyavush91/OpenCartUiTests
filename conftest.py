import os
import urllib.parse

import pytest
from selenium import webdriver
import logging
import datetime
from browsermobproxy import Server, Client
from selenium.webdriver import ChromeOptions, FirefoxOptions, DesiredCapabilities
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost:8888/Opencart/opencart-3.0.3.2/upload/", help="choose your browser")
    parser.addoption("--waiting", action="store", help="Time which browser will wait elements", default=10, required=False)


@pytest.fixture(scope="session")
def url(request):
    "Фикстура для получения URL"
    return request.config.getoption("--url")


# @pytest.fixture(scope="session")
# def proxy():
#     """Фикстура для конфигурирования прокси-сервера"""
#     server = Server('/Users/penguin/Tools/browsermob-proxy-2.1.4/bin/browsermob-proxy')
#     server.start()
#     client = Client("localhost:8080")
#     client.new_har()
#     return server, client


@pytest.fixture(scope="session")
def browser(request):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    waiting = request.config.getoption("--waiting")
    # url = urllib.parse.urlparse(proxy[1].proxy).path

    if browser == "chrome":
        options = ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--start-fullscreen')
        # options.add_argument('--proxy-server=%s' % url)
        options.add_experimental_option('w3c', False)
        caps = DesiredCapabilities.CHROME
        caps['timeouts'] = {'implicit': 20000, 'pageLoad': 20000, 'script': 20000}
        driver = EventFiringWebDriver(webdriver.Chrome(options=options, desired_capabilities=caps), MyListener())
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    browser_logging(driver)
    # proxy_logging(proxy[1])
    driver.implicitly_wait(waiting)
    request.addfinalizer(driver.close)

    return driver


@pytest.fixture(scope="session")
def simple_logger():
    """Фикстура логгирования - запись в файл и вывод в консоль на разных уровнях"""

    logger = logging.getLogger("Simple")
    logger.setLevel(logging.DEBUG)

    console_log = logging.StreamHandler()
    console_log.setLevel(logging.INFO)


    file_log = logging.FileHandler("/Users/penguin/PycharmProjects/OpenTests/logs/testing.log")
    file_log.setLevel(logging.INFO)

    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_log.setFormatter(log_format)
    file_log.setFormatter(log_format)

    logger.addHandler(console_log)
    logger.addHandler(file_log)

    return logger

class MyListener(AbstractEventListener):
    """Логирование Webdriver"""

    logging.basicConfig(filename="/Users/penguin/PycharmProjects/OpenTests/logs/opencart_testing_webdriver.log",
                        level=logging.ERROR)

    def before_find(self, by, value, driver):
        """Логирование перед нахождением элемента"""
        logging.error("Opening element " + by + value)

    def after_find(self, by, value, driver):
        """Логирование после нахождения элемента"""
        logging.info("Find element " + by + value)

    def on_exception(self, exception, driver):
        """Логирование на Exception, создание скриншота"""
        now = datetime.datetime.now().strftime("%d-%m-%y-")
        message = str(now) + driver.name + '_' + exception.msg
        path = "/Users/penguin/PycharmProjects/OpenTests/screenshots/" + message[:30] + ".png"
        driver.save_screenshot(path)
        logging.error(message)
        logging.error(path)


def proxy_logging(proxy):
    """Запись лога прокси сервера"""
    with open("/Users/penguin/PycharmProjects/OpenTests/logs/opencart_testing_proxy.log", "a") as file:
        params = proxy.har["log"]
        for key in params:
            message = str(key) + " -- " + str(params[key]) + "\n"
            file.write(message)



def browser_logging(browser):
    with open("/Users/penguin/PycharmProjects/OpenTests/logs/opencart_testing_browser.log", "a") as file:
       for line in browser.get_log('browser'):
            file.write(str(line))
