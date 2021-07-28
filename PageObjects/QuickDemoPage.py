from selenium.webdriver.common.by import By


class QuickDemoPage:
    def __init__(self, driver):
        self.driver = driver

    fname = (By.ID, "wdform_1_element_first2")
    lname = (By.ID, "wdform_1_element_last2")
    email = (By.CSS_SELECTOR, "input#wdform_2_element2")
    contact = (By.CSS_SELECTOR, "input#wdform_4_element2")
    date = (By.CSS_SELECTOR, "input#wdform_10_element2")
    courses = (By.CSS_SELECTOR, "select#wdform_5_element2")
    submit = (By.CSS_SELECTOR, "button.button-submit")
    message = (By.CSS_SELECTOR, "dd.message")

    def getFirstName(self):
        return self.driver.find_element(*QuickDemoPage.fname)

    def getLastName(self):
        return self.driver.find_element(*QuickDemoPage.lname)

    def getEmail(self):
        return self.driver.find_element(*QuickDemoPage.email)

    def getContact(self):
        return self.driver.find_element(*QuickDemoPage.contact)

    def getDate(self):
        return self.driver.find_element(*QuickDemoPage.date)

    def getCourses(self):
        return self.driver.find_element(*QuickDemoPage.courses)

    def getSubmitBtn(self):
        return self.driver.find_element(*QuickDemoPage.submit)

    def getMessage(self):
        return self.driver.find_element(*QuickDemoPage.message)