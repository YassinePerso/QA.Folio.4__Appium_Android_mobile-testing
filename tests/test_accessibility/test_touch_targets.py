from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage


MIN_TOUCH_TARGET_PX = 48


def get_size(element):
    rect = element.rect
    return rect["width"], rect["height"]


def test_cart_action_buttons_meet_minimum_touch_size(driver):
    """
    Vérifie que les boutons d'action du panier (quantité +/-, suppression)
    respectent la taille minimale recommandée par Android pour une cible
    tactile (48px), essentielle pour les utilisateurs à motricité réduite.
    """
    products_page = ProductsPage(driver)
    products_page.open_first_product()
    products_page.add_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)

    minus_w, minus_h = get_size(cart_page.find(cart_page.MINUS_BUTTON))
    plus_w, plus_h = get_size(cart_page.find(cart_page.PLUS_BUTTON))

    print(f"Bouton diminuer: {minus_w}x{minus_h}px")
    print(f"Bouton augmenter: {plus_w}x{plus_h}px")

    assert minus_w >= MIN_TOUCH_TARGET_PX and minus_h >= MIN_TOUCH_TARGET_PX, \
        f"Bouton diminuer trop petit: {minus_w}x{minus_h}px (minimum {MIN_TOUCH_TARGET_PX}px)"
    assert plus_w >= MIN_TOUCH_TARGET_PX and plus_h >= MIN_TOUCH_TARGET_PX, \
        f"Bouton augmenter trop petit: {plus_w}x{plus_h}px (minimum {MIN_TOUCH_TARGET_PX}px)"
        
        
def test_header_icons_meet_minimum_touch_size(driver):
    """
    Vérifie la taille des icônes du header (menu, panier), souvent les
    plus petites de l'interface car contraintes par l'espace disponible.
    """
    products_page = ProductsPage(driver)

    menu_w, menu_h = get_size(products_page.find(
        "com.saucelabs.mydemoapp.android:id/menuIV"
    ))
    cart_w, cart_h = get_size(products_page.find(products_page.CART_ICON))

    print(f"Icône menu: {menu_w}x{menu_h}px")
    print(f"Icône panier: {cart_w}x{cart_h}px")

    assert menu_w >= MIN_TOUCH_TARGET_PX and menu_h >= MIN_TOUCH_TARGET_PX, \
        f"Icône menu trop petite: {menu_w}x{menu_h}px"
    assert cart_w >= MIN_TOUCH_TARGET_PX and cart_h >= MIN_TOUCH_TARGET_PX, \
        f"Icône panier trop petite: {cart_w}x{cart_h}px"
