import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

def test_app_launches():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "pixel_test"
    options.app_package = "com.saucelabs.mydemoapp.android"
    options.app_activity = ".view.activities.SplashActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    assert driver.current_package == "com.saucelabs.mydemoapp.android"

    driver.quit()