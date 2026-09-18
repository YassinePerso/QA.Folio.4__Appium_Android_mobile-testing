from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    #Trouve un élément par son ID
    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, locator))
        )

    #Clique sur un élément
    def click(self, locator):
        self.find(locator).click()

    #Tape du texte dans un champ
    def type_text(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
    
    #Trouve un élément par son ID d'accessibilité
    def find_by_acc_id(self, acc_id):
        return self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, acc_id))
        )

    #Clique sur un élément par son ID d'accessibilité
    def click_by_acc_id(self, acc_id):
        self.find_by_acc_id(acc_id).click()