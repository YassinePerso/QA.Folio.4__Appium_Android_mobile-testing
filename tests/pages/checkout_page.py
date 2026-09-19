from .base_page import BasePage


class CheckoutPage(BasePage):
    TITLE = "com.saucelabs.mydemoapp.android:id/checkoutTitleTV"
    TO_PAYMENT_BUTTON = "com.saucelabs.mydemoapp.android:id/paymentBtn"

    #Récupère le titre de la page de paiement
    def get_title(self):
        return self.find(self.TITLE).text

    #Clique sur le bouton pour passer à la page de paiement
    def go_to_payment(self):
        self.click(self.TO_PAYMENT_BUTTON)