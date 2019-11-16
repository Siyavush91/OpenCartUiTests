from locators import Catalog, Alert
from .BasePage import BasePage


class AdminProducts(BasePage):

    def open(self):
        """Открытие панели администратора"""
        self._open("/admin")
        return self

    def open_product_page(self):
        self._click(Catalog.navigation.catalog_outs)
        self._click(Catalog.edit_products.products)

    def add_product(self):
        self._click(Catalog.edit_products.add_new_product)

    def product_filter(self, text):
        self._clear_element_(Catalog.filter_product.input_product_name)
        self._input(Catalog.filter_product.input_product_name, value=text)
        self._click(Catalog.filter_product.accept_filter)

    def click_firstline_checkbox(self):
        self._click(Catalog.productList.product_check_box)

    def delete_product(self):
        self._click(Catalog.edit_products.delete_product)

    def check_alert(self):
        self._wait_for_visible(Alert.success.it)

    def alert_present(self):
        self._wait_for_alert()

    def edit_product(self):
        self._click(Catalog.productList.edit_product)










