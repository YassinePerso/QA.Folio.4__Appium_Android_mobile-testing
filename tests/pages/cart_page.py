from .base_page import BasePage


class CartPage(BasePage):
    ITEM_TITLE = "com.saucelabs.mydemoapp.android:id/titleTV"
    ITEMS_COUNT = "com.saucelabs.mydemoapp.android:id/itemsTV"
    CHECKOUT_BUTTON = "com.saucelabs.mydemoapp.android:id/cartBt"


    #Récupère le titre de l'article dans le panier
    def get_item_title(self):
        return self.find(self.ITEM_TITLE).text

    #Récupère le nombre d'articles dans le panier
    def get_items_count_text(self):
        return self.find(self.ITEMS_COUNT).text
    
    #Clique sur le bouton de paiement pour passer à la page de paiement
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)