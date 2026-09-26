from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage


def test_increase_quantity(driver):
    products_page = ProductsPage(driver)
    products_page.open_first_product()
    products_page.add_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_quantity() == "1"

    cart_page.increase_quantity()
    assert cart_page.get_quantity() == "2"


def test_decrease_quantity(driver):
    products_page = ProductsPage(driver)
    products_page.open_first_product()
    products_page.add_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.increase_quantity()
    assert cart_page.get_quantity() == "2"

    cart_page.decrease_quantity()
    assert cart_page.get_quantity() == "1"


def test_remove_item_empties_cart(driver):
    products_page = ProductsPage(driver)
    products_page.open_first_product()
    products_page.add_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.remove_item()

    assert cart_page.is_cart_empty()
