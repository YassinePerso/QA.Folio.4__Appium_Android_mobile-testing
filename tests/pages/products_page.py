from .base_page import BasePage


class ProductsPage(BasePage):
    FIRST_PRODUCT = "com.saucelabs.mydemoapp.android:id/productIV"
    ADD_TO_CART_BUTTON = "com.saucelabs.mydemoapp.android:id/cartBt"
    CART_ICON = "com.saucelabs.mydemoapp.android:id/cartRL"
    CART_BADGE = "com.saucelabs.mydemoapp.android:id/cartTV"


    #Ouvre le premier produit "sauce labs backpack"
    def open_first_product(self):
        self.click(self.FIRST_PRODUCT)

    #Ajout au panier
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    #Ouverture du panier
    def open_cart(self):
        self.click(self.CART_ICON)
        
    #Récupère le nombre d'articles dans le panier
    def get_cart_count(self):
        return self.find(self.CART_BADGE).text