import pytest

from page_object import AdminProducts, AdminLogin, ProductDescriptionPage

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
class TestCreateProducts:

    def test_open_catalog(self, browser):
        """
        Тест открытия экрана c продуктом
        """
        open_products = AdminProducts(browser)
        open_products.open_product_page()


    def test_add_new(self, browser):
        """
        Тест добавления нового продукта
        """
        open_add_product = AdminProducts(browser)
        add_product = ProductDescriptionPage(browser)
        open_add_product.add_product()
        add_product.input_productname("IphoneXR")
        add_product.input_productdescript("Something about it!!!")
        add_product.input_metatitle("Iphone XR")
        add_product.open_data_tab()
        add_product.input_modelfield("10RK")
        add_product.save_product()
        open_add_product.check_alert()


#
#     def test_edit(self, browser):
#         """
#             Тестирование редактирования первого продукта из списка
#         """
#         browser.find_element_by_xpath(Catalog.edit_product).click()
#         nav_tab = browser.find_elements_by_css_selector(Catalog.product_nav_tabs)
#         for item in nav_tab:
#             ActionChains(browser).move_to_element(item).pause(1).perform()
#         browser.find_element_by_xpath(Catalog.save_button).click()
#         assert browser.find_elements_by_xpath(Alerts.add_to_wish_alert)
#
#
    def test_delete(self, browser):
        """
            Тест удаления добавленного продукта
        """
        delete_product = AdminProducts(browser)
        delete_product.product_filter("IphoneXR")
        delete_product.click_firstline_checkbox()
        delete_product.delete_product()
        delete_product.alert_present()
        Alert(browser).accept()
