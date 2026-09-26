import time
from PIL import Image
from tests.pages.products_page import ProductsPage


def relative_luminance(rgb):
    """Formule WCAG 2.x de luminance relative."""
    def channel(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast_ratio(rgb1, rgb2):
    """Formule WCAG du ratio de contraste, entre 1:1 et 21:1."""
    l1 = relative_luminance(rgb1)
    l2 = relative_luminance(rgb2)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def test_product_title_contrast_on_catalog(driver):
    """
    Mesure le contraste réel du titre produit (texte noir sur fond blanc,
    zone sûre) via une capture d'écran et la formule WCAG officielle.
    Seuil AA texte normal : 4.5:1 (RGAA critère 3.2, transposé du web).
    """
    products_page = ProductsPage(driver)

    title_element = products_page.find(
        "com.saucelabs.mydemoapp.android:id/titleTV"
    )
    rect = title_element.rect
    print("Bounds élément:", rect)

    # Laisse le rendu graphique se stabiliser avant la capture
    # (rendu logiciel SwiftShader plus lent que l'arbre d'accessibilité)
    time.sleep(1)

    driver.save_screenshot("/tmp/catalog_screenshot.png")
    img = Image.open("/tmp/catalog_screenshot.png").convert("RGB")

    left, top = rect["x"], rect["y"]
    right, bottom = left + rect["width"], top + rect["height"]
    print("Zone de découpe:", (left, top, right, bottom))

    region = img.crop((left, top, right, bottom))
    pixels = list(region.getdata())

    text_color = min(pixels, key=lambda p: sum(p))
    background_color = max(pixels, key=lambda p: sum(p))

    ratio = contrast_ratio(text_color, background_color)
    print(f"Texte: {text_color}, Fond: {background_color}, Ratio: {ratio:.2f}:1")

    assert ratio >= 4.5, f"Contraste insuffisant: {ratio:.2f}:1 (minimum AA: 4.5:1)"