from page_object import MainPage

def test_user_auth(browser):
    user_login = MainPage(browser)
    user_login.open_login_page()
    user_login.verify_login_form()
