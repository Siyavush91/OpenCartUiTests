from locators import Login, Catalog, ProductDescription, Alert
from .BasePage import BasePage


class ProductDescriptionPage(BasePage):

    def input_productname(self, text):
        self._input(ProductDescription.product_name_field, value=text)

    def input_productdescript(self, text):
        self._clear_element_(ProductDescription.product_description_field)
        self._input(ProductDescription.product_description_field, value=text)

    def input_metatitle(self, text):
        self._clear_element_(ProductDescription.meta_tag_title)
        self._input(ProductDescription.meta_tag_title, value=text)

    def open_data_tab(self):
        self._click(ProductDescription.data_tab)

    def input_modelfield(self, text):
        self._clear_element_(ProductDescription.model_field)
        self._input(ProductDescription.model_field, text)

    def save_product(self):
        self._click(ProductDescription.save_button)

    def cancel_add(self):
        self._click(ProductDescription.cancel_button)

    def open_image_tab(self):
        self._click(ProductDescription.image_tab)

    def click_image(self):
        self._click(ProductDescription.image_button)

    def edit_image(self):
        self._click(ProductDescription.edit_image)

    def add_image(self, file):
        self._input(ProductDescription.download_image, file, 1)

    def verify_element(self):
        self._wait_for_visible(ProductDescription.button_upload)


    def check_modal_text(self):
        self._get_element_text(ProductDescription.modalka)

    def choose_im(self):
        self._click(ProductDescription.im)

