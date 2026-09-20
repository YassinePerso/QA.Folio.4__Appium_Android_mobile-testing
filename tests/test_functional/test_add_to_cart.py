from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage


def test_add_product_to_cart(driver):
    products_page = ProductsPage(driver)
    products_page.open_first_product()
    products_page.add_to_cart()

    assert products_page.get_cart_count() == "1"

    products_page.open_cart()
    cart_page = CartPage(driver)

    assert cart_page.get_item_title() == "Sauce Labs Backpack"
    assert cart_page.get_items_count_text() == "1 Items"