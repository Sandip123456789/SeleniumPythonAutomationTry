import pytest
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):
    def test_homePage(self):
        driver = self.driver

        log = self.getLogger()

        # creating objects
        homePage = HomePage(driver)

        log.info("Title: "+driver.title)

        log.info("Scrolling to bottom")
        # scroll bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # phone number
        phone = homePage.getPhoneNumber().text
        # print(phone)
        log.info(phone)
        # email
        email = homePage.getEmail().text
        # print(email)
        log.info(email)

        log.info("Scrolling to top")
        # scroll top
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")