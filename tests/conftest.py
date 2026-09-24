import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


APP_PACKAGE = "com.saucelabs.mydemoapp.android"
APP_ACTIVITY = ".view.activities.SplashActivity"


@pytest.fixture(scope="session")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "pixel_test"
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY

    d = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield d
    d.quit()


@pytest.fixture(autouse=True)
def reset_app_state(driver):
    """
    Réinitialise l'état de l'app entre chaque test sans recréer toute la
    session Appium. Une seule session est ouverte pour toute la suite (voir
    fixture driver), ce qui évite de refaire à chaque test le cycle lourd
    d'installation du serveur UiAutomator2, qui a fini par crasher le
    system_server Android en CI lorsqu'il était répété 12 fois d'affilée.

    'mobile: clearApp' vide les données de l'app (panier, session de
    connexion) sans réinstaller le serveur d'automatisation, contrairement
    au comportement automatique qu'offrait une nouvelle session Appium.
    """
    driver.terminate_app(APP_PACKAGE)
    driver.execute_script("mobile: clearApp", {"appId": APP_PACKAGE})
    driver.activate_app(APP_PACKAGE)
    time.sleep(1.5)
    yield