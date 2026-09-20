from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage

# Test pour vérifier que l'application survit à la mise en arrière-plan
def test_app_survives_background(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.type_text(login_page.USERNAME_FIELD, "bod@example.com")

    #Met l'application en arrière-plan pendant 5 secondes
    driver.background_app(5)

    field = login_page.find(login_page.USERNAME_FIELD)
    assert field.text == "bod@example.com"
    
    
# Test pour vérifier que le panier survit à la mise en arrière-plan
def test_cart_survives_background(driver):
    products_page = ProductsPage(driver)
    products_page.open_first_product()
    products_page.add_to_cart()

    assert products_page.get_cart_count() == "1"
    driver.background_app(5)
    assert products_page.get_cart_count() == "1"
    

# Test pour vérifier que l'application revient correctement après une courte mise en arrière-plan  
def test_short_background_return(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.type_text(login_page.USERNAME_FIELD, "bod@example.com")

    #mise en arrière-plan pendant 1 seconde
    driver.background_app(1)
    field = login_page.find(login_page.USERNAME_FIELD)
    assert field.text == "bod@example.com"
    

# Test pour vérifier que l'application revient correctement après plusieurs cycles de mise en arrière-plan
def test_multiple_background_cycles(driver):
    products_page = ProductsPage(driver)
    products_page.open_first_product()
    products_page.add_to_cart()

    #boucle pour mettre l'application en arrière-plan et vérifier que le panier reste intact
    for _ in range(3):
        driver.background_app(2)
        assert products_page.get_cart_count() == "1"