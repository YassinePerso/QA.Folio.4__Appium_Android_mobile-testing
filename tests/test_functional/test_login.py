from tests.pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("bod@example.com", "10203040")