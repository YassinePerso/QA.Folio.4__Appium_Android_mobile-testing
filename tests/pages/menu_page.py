from .base_page import BasePage


class MenuPage(BasePage):
    MENU_BUTTON = "com.saucelabs.mydemoapp.android:id/menuIV"

    # Ouvre le menu de l'application
    def open_menu(self):
        self.click(self.MENU_BUTTON)

    # Ouvre le scanner de code QR depuis le menu
    def open_qr_scanner(self):
        self.open_menu()
        self.click_by_text("QR Code Scanner")
        