from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    phone = (By.CLASS_NAME, "phone")
    email = (By.LINK_TEXT, "thetestingworld@gmail.com")
    button= (By.LINK_TEXT, "Quick Demo")

    def getPhoneNumber(self):
        return self.driver.find_element(*HomePage.phone)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getQuickLinkBtn(self):
        return self.driver.find_element(*HomePage.button)