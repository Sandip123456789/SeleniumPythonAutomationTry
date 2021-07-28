from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import pytest

from PageObjects.HomePage import HomePage
from PageObjects.QuickDemoPage import QuickDemoPage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self, getData):
        driver = self.driver

        #creating objects
        homePage = HomePage(driver)
        quickdemoPage = QuickDemoPage(driver)

        # scroll bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        #phone number
        phone = homePage.getPhoneNumber().text
        print(phone)
        #email
        email = homePage.getEmail().text
        print(email)

        # scroll top
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

        #quick demo button
        homePage.getQuickLinkBtn().click()

        quickdemoPage.getFirstName().send_keys(getData["fname"])
        quickdemoPage.getLastName().send_keys(getData["lname"])
        quickdemoPage.getEmail().send_keys(getData["email"])
        quickdemoPage.getContact().send_keys(getData["contact"])
        quickdemoPage.getDate().send_keys(getData["date"])

        # for static dropdown use Select
        # select = Select(quickdemoPage.getCourses())
        # select.select_by_visible_text("DevOps")

        #static dropdown called from BaseClass
        self.selectDropdownByText(quickdemoPage.getCourses(), "Python")

        quickdemoPage.getSubmitBtn().click()

        successMessage = quickdemoPage.getMessage().text
        assert "successfully submitted" in successMessage
        print(successMessage)

        # refresh before second test inputs in case page doesn't refresh after hitting submit button
        # self.driver.refresh()

    #parameterizing
    @pytest.fixture(params=[
        {"fname": "Allison", "lname": "Becker", "email": "AB1@gmail.com", "contact": "07775218999", "date": "1999-07-07"},
        {"fname": "Vergil", "lname": "Van Dijk", "email": "vergil4@gmail.com", "contact": "06665217888", "date": "1995-08-07"}
    ])
    def getData(self, request):
        return request.param