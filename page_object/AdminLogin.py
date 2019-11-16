from locators import Login
from page_object.BasePage import BasePage
import logging



class AdminLogin(BasePage):

    def open(self):
        """Открытие панели администратора"""
        self._open("/admin")
        return self

    def input_username(self, text):
        self._clear_element_(Login.user_name_field)
        self._input(Login.user_name_field, value=text)
        return self

    def input_password(self, password):
        self._clear_element_(Login.password_field)
        self._input(Login.password_field, value=password)
        return self

    def submit_login(self):
        self._click(Login.login_button)
        return self
