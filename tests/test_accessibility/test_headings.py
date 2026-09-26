import xml.etree.ElementTree as ET
from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage


def get_heading_attribute(driver, resource_id):
    """Cherche un élément par resource-id dans le page_source et retourne son attribut heading."""
    root = ET.fromstring(driver.page_source)
    for node in root.iter():
        if node.attrib.get("resource-id") == resource_id:
            return node.attrib.get("heading")
    return None


def test_screen_titles_are_marked_as_headings(driver):
    """
    Vérifie que les titres d'écran (Products, Login) sont marqués
    heading="true" dans l'arbre d'accessibilité, ce qui permet à TalkBack
    de naviguer directement entre les sections principales d'une app.

    Principe RGAA concerné (transposé du web au mobile) : critère 9.1,
    structuration de l'information par des titres.
    """
    # L'écran produits est l'écran de départ après reset, pas besoin de naviguer
    products_heading = get_heading_attribute(driver, "com.saucelabs.mydemoapp.android:id/productTV")
    print("Products title heading:", repr(products_heading))

    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_heading = get_heading_attribute(driver, "com.saucelabs.mydemoapp.android:id/loginTV")
    print("Login title heading:", repr(login_heading))

    # On documente les deux résultats réels, qu'ils soient bons ou mauvais
    assert products_heading == "true", f"Le titre 'Products' n'est pas marqué comme heading (valeur: {products_heading})"
    assert login_heading == "true", f"Le titre 'Login' n'est pas marqué comme heading (valeur: {login_heading})"