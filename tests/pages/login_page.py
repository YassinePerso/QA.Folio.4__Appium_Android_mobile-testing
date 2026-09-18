from .base_page import BasePage


class LoginPage(BasePage):
    MENU_BUTTON = "com.saucelabs.mydemoapp.android:id/menuIV"
    LOGIN_MENU_ITEM = "Login Menu Item"
    USERNAME_FIELD = "com.saucelabs.mydemoapp.android:id/nameET"
    PASSWORD_FIELD = "com.saucelabs.mydemoapp.android:id/passwordET"
    LOGIN_BUTTON = "com.saucelabs.mydemoapp.android:id/loginBtn"

    #Navigue vers la page loginS
    def navigate_to_login(self):
        self.click(self.MENU_BUTTON)
        self.click_by_acc_id(self.LOGIN_MENU_ITEM)

    #Algo qui permet l'action complète de login
    def login(self, username, password):
        self.navigate_to_login()
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)