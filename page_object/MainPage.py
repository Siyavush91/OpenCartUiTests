from locators import Common
from .BasePage import BasePage
from .ProductPage import ProductPage

class MainPage(BasePage):

    def open_login_page(self):
        self._click(Common.nav_top.my_account_drop)
        self._click(Common.nav_top.login_button)


    def verify_login_form(self):
        self._wait_for_visible(Common.nav_top.login_form)









    # def click_featured_product(self, number):
    #     index = number - 1
    #     self._click(Main.featured.products, index=index)
    #     return ProductPage(self.driver)
    #
    # def get_featured_product_name(self, number):
    #     index = number - 1
    #     return self._get_element_text(Main.featured.names, index=index)
