from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import pytest
from TestData.QuickDemoPageData import QuickDemoPageData
from PageObjects.HomePage import HomePage
from PageObjects.QuickDemoPage import QuickDemoPage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self, getData):
        driver = self.driver

        log = self.getLogger()

        #creating objects
        homePage = HomePage(driver)
        quickdemoPage = QuickDemoPage(driver)

        # log.info("Scrolling to bottom")
        # # scroll bottom
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #
        # #phone number
        # phone = homePage.getPhoneNumber().text
        # # print(phone)
        # log.info(phone)
        # #email
        # email = homePage.getEmail().text
        # # print(email)
        # log.info(email)
        #
        # log.info("Scrolling to top")
        # # scroll top
        # driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        #
        # #quick demo button
        # homePage.getQuickLinkBtn().click()

        # quick demo button
        homePage.getQuickLinkBtn().click()

        log.info("Entered first name is "+getData["fname"]+" and last name is "+getData["lname"])
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
        # print(successMessage)
        log.info(successMessage)

        # refresh before second test inputs in case page doesn't refresh after hitting submit button
        # self.driver.refresh()

    #parameterizing
    @pytest.fixture(params=QuickDemoPageData.test_quickDemo_data)
    def getData(self, request):
        return request.param