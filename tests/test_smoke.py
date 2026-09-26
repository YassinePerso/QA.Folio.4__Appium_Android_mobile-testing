def test_app_launches(driver):
    assert driver.current_package == "com.saucelabs.mydemoapp.android"