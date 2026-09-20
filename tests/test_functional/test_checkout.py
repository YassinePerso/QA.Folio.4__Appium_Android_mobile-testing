from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage

#Test complet pour vérifier le flux de paiement
def test_checkout_flow_starts(driver):
    login_page = LoginPage(driver)
    login_page.login("bod@example.com", "10203040")

    products_page = ProductsPage(driver)
    products_page.open_first_product()
    products_page.add_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    assert checkout_page.get_title() == "Checkout"