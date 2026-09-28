from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage


def is_missing_label(value):
    return value in (None, "", "null")


def test_cart_action_buttons_have_labels(driver):
    """
    Vérifie que les boutons d'action du panier (quantité, suppression)
    sont correctement labellisés pour un lecteur d'écran.
    """
    products_page = ProductsPage(driver)
    products_page.open_first_product()
    products_page.add_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)

    minus_label = cart_page.find(cart_page.MINUS_BUTTON).get_attribute("content-desc")
    plus_label = cart_page.find(cart_page.PLUS_BUTTON).get_attribute("content-desc")
    remove_label = cart_page.find(cart_page.REMOVE_BUTTON).get_attribute("content-desc")

    assert not is_missing_label(minus_label), "Le bouton diminuer quantité n'a pas de content-desc"
    assert not is_missing_label(plus_label), "Le bouton augmenter quantité n'a pas de content-desc"
    assert not is_missing_label(remove_label), "Le bouton supprimer n'a pas de content-desc"