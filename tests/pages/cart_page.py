from .base_page import BasePage


class CartPage(BasePage):
    ITEM_TITLE = "com.saucelabs.mydemoapp.android:id/titleTV"
    ITEMS_COUNT = "com.saucelabs.mydemoapp.android:id/itemsTV"
    CHECKOUT_BUTTON = "com.saucelabs.mydemoapp.android:id/cartBt"
    MINUS_BUTTON = "com.saucelabs.mydemoapp.android:id/minusIV"
    PLUS_BUTTON = "com.saucelabs.mydemoapp.android:id/plusIV"
    REMOVE_BUTTON = "com.saucelabs.mydemoapp.android:id/removeBt"
    QUANTITY_TEXT = "com.saucelabs.mydemoapp.android:id/noTV"
    NO_ITEMS_TITLE = "com.saucelabs.mydemoapp.android:id/noItemTitleTV"


    #Récupère le titre de l'article dans le panier
    def get_item_title(self):
        return self.find(self.ITEM_TITLE).text

    #Récupère le nombre d'articles dans le panier
    def get_items_count_text(self):
        return self.find(self.ITEMS_COUNT).text
    
    #Clique sur le bouton de paiement pour passer à la page de paiement
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        
    #Récupère la quantité de l'article dans le panier
    def get_quantity(self):
        return self.find(self.QUANTITY_TEXT).text

    #Clique sur le bouton "+" pour augmenter la quantité de l'article dans le panier
    def increase_quantity(self):
        self.click(self.PLUS_BUTTON)

    #Clique sur le bouton "-" pour diminuer la quantité de l'article dans le panier
    def decrease_quantity(self):
        self.click(self.MINUS_BUTTON)

    #Clique sur le bouton "Remove" pour supprimer l'article du panier
    def remove_item(self):
        self.click(self.REMOVE_BUTTON)

    #Vérifie si le panier est vide en comparant le texte affiché avec "No Items"
    def is_cart_empty(self):
        return self.find(self.NO_ITEMS_TITLE).text == "No Items"