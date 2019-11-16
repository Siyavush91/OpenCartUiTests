from locators import Common
from .BasePage import BasePage
from .ProductPage import ProductPage

class LoginPage(BasePage):

    def login_user(self, email, password):
        self._input(Common.user_login.email_input, email)
        self._input(Common.user_login.password_input, password)
        self._click(Common.user_login.login_button)

    def verify_login_form(self):
        self._wait_for_visible(Common.nav_top.login_form)

