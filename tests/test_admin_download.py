import os
import pytest
import time
from page_object import DownloadPage, AdminLogin, AdminDownloads
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert


@pytest.fixture(scope="module")
def login(browser, url, simple_logger):
    """Тест на авторизацию в админке"""
    AdminLogin(browser, url)\
        .open() \
        .input_username("admin") \
        .input_password("25191") \
        .submit_login()


@pytest.mark.usefixtures("login")
class TestDownloadProducts:

    def test_download(self, browser):
        """Открываем страницу Downloads"""
        open_downloads = AdminDownloads(browser)
        open_downloads.open_downloads_page()

    def test_add_download(self, browser):
        """Добавляем форму через JS и файл с фото формата PNG. Файл лежит в корне проекта"""
        p_name = "New Iphone"
        p_meta_teg_title = "ios"
        p_model = "HUGEGGG"
        p_photo = "image_2019-09-03_17-28-17.png"

        add_download = AdminDownloads(browser)
        #переходим в Admin/Downloads
        add_download.open_downloads_page()
        #Открываем добавление файла
        add_download.add_download()
        #Добавляем файл
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, p_photo)
        #добавляем форму через JS
        browser.execute_script("""document.getElementById("button-upload").click();
        var f = document.createElement("form");
        f.enctype = "multipart/form-data";
	    f.id = "form-upload";
        f.style.display = "block";
        inp = document.createElement("input");
        inp.type = "file";
        inp.name = "file";
        f.appendChild(inp);
        body = document.getElementsByTagName("body")[0];
        body.insertBefore(f, body.firstChild); """)
        #находим селектор формы добавленной через JS
        element = browser.find_element_by_css_selector("input[type=file]")
        time.sleep(10)
        #отправляем файл
        element.send_keys(filename)

        #Заполнили все поля в форме
        input_download = DownloadPage(browser)
        input_download.input_down_name(p_name)
        input_download.input_filename(p_model)
        input_download.input_meta(p_meta_teg_title)

        input_download.click_savebutton()
        time.sleep(10)
