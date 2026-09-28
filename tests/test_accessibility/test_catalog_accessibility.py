from tests.pages.products_page import ProductsPage


def is_missing_label(value):
    return value in (None, "", "null")


def test_catalog_key_elements_have_labels(driver):
    """
    Vérifie que les éléments clés du catalogue (icône panier, image produit)
    ont un content-desc exploitable par un lecteur d'écran.
    """
    products_page = ProductsPage(driver)

    cart_icon = products_page.find(products_page.CART_ICON)
    product_image = products_page.find(products_page.FIRST_PRODUCT)

    cart_label = cart_icon.get_attribute("content-desc")
    product_label = product_image.get_attribute("content-desc")

    assert not is_missing_label(cart_label), "L'icône panier n'a pas de content-desc"
    assert not is_missing_label(product_label), "L'image produit n'a pas de content-desc"
