from tests.pages.menu_page import MenuPage

# Test pour vérifier que l'application reste au premier plan après avoir refusé la permission de la caméra
def test_camera_permission_denied(driver):
    menu_page = MenuPage(driver)
    menu_page.open_qr_scanner()

    # Premier refus
    menu_page.click_by_text("Don’t allow")

    # Android redemande une seconde fois après un premier refus
    menu_page.click_by_text("Don’t allow")
    assert driver.current_package == "com.saucelabs.mydemoapp.android"
    
# Test pour vérifier que l'application reste au premier plan après avoir accordé la permission de la caméra
def test_camera_permission_granted(driver):
    menu_page = MenuPage(driver)
    menu_page.open_qr_scanner()
    menu_page.click_by_text("While using the app")

    # Après acceptation, l'app reste au premier plan (pas de redirection vers un écran d'erreur)
    assert driver.current_package == "com.saucelabs.mydemoapp.android"