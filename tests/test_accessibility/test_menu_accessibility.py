from appium.webdriver.common.appiumby import AppiumBy
from tests.pages.menu_page import MenuPage


def is_missing_label(value):
    return value in (None, "", "null")


def test_menu_items_have_labels(driver):
    menu_page = MenuPage(driver)
    menu_page.open_menu()

    catalog_item = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Catalog")'
    )
    qr_item = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("QR Code Scanner")'
    )

    catalog_label = catalog_item.get_attribute("content-desc")
    qr_label = qr_item.get_attribute("content-desc")

    # On documente le résultat réel, qu'il soit bon ou mauvais
    print("Catalog content-desc:", repr(catalog_label))
    print("QR Code Scanner content-desc:", repr(qr_label))

    assert not is_missing_label(catalog_label), "L'item 'Catalog' du menu n'a pas de content-desc distinct"
    assert not is_missing_label(qr_label), "L'item 'QR Code Scanner' du menu n'a pas de content-desc distinct"
