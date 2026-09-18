from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = "com.saucelabs.mydemoapp.android:id/nameET"
    PASSWORD_FIELD = "com.saucelabs.mydemoapp.android:id/passwordET"
    LOGIN_BUTTON = "com.saucelabs.mydemoapp.android:id/loginBtn"


    #Action complète pour se connecter à l'application
    def login(self, username, password):
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)