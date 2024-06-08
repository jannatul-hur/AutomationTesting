import pytest
from selenium.webdriver import Keys
import time
from pageObjects.addTicketPage import AddTicketPage
from pageObjects.loginPage import LoginPage
from testData.loginPageData import LoginPageData
from utilities.BaseClass import BaseClass

class TestLoginWithWrongPassword(BaseClass):
    def test_loginWithWrongPassword(self, getUserData):
        log = self.getLogger()
        log.info("Step-1: Opening the Ticketing Page")
        # Instantiating the AddTicketPage class passing the current webdriver object
        addTicketPage = AddTicketPage(self.driver)
        time.sleep(3)

        # Step-2: Click on the "Login" button
        log.info("Step-2: Clicking on the Login Button")
        loginPage = addTicketPage.getLoginButton()
        time.sleep(3)

        # Step-3: Enter the email
        log.info("Step-3: Entering the Email Address")
        loginPage.getEmailField().send_keys(getUserData["email"])
        time.sleep(3)

        # Step-4: Enter the Wrong password
        log.info("Step-4: Entering the Wrong Password")
        loginPage.getPasswordField().send_keys(getUserData["password"])
        time.sleep(3)

        # Step-5: Check the remember me checkbox
        log.info("Step-5: Checking the remember me checkbox")
        loginPage.getRememberMeChcekbox().click()
        time.sleep(3)

        # Step-5: Click on the Login button
        log.info("Step-6: Clicking the Login Button")
        dashboardPage = loginPage.getLoginButton()
        time.sleep(3)

        # Verifying the login has failed
        wrongPasswordAlertText = loginPage.getWrongPasswordlAlertText().text
        assert ("These credentials do not match our records." in wrongPasswordAlertText)

    @pytest.fixture(params=LoginPageData.test_loginPage_data_wrong_password)
    def getUserData(self, request):
        return request.param