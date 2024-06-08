import pytest
from selenium.webdriver import Keys
import time
from pageObjects.addTicketPage import AddTicketPage
from pageObjects.loginPage import LoginPage
from testData.loginPageData import LoginPageData
from utilities.BaseClass import BaseClass


class TestLoginWithRemember(BaseClass):
    def test_loginWithRemember(self, getUserData):
        log = self.getLogger()
        log.info("Step-1: Opening the Ticketing Page")
        # Instantiating the AddTicketPage class passing the current webdriver object
        addTicketPage = AddTicketPage(self.driver)
        time.sleep(5)

        # Step-2: Click on the "Login" button
        log.info("Step-2: Clicking on the Login Button")
        loginPage = addTicketPage.getLoginButton()

        # Step-3: Enter the email
        log.info("Step-3: Entering the Invalid Email Address")
        loginPage.getEmailField().send_keys(getUserData["email"])
        time.sleep(5)

        # Step-4: Enter the password
        log.info("Step-4: Entering the Password")
        loginPage.getPasswordField().send_keys(getUserData["password"])

        # Step-5: Check the remember me checkbox
        log.info("Step-5: Checking the remember me checkbox")
        loginPage.getRememberMeChcekbox().click()
        time.sleep(5)

        # Step-5: Click on the Login button
        log.info("Step-6: Clicking the Login Button")
        dashboardPage = loginPage.getLoginButton()
        time.sleep(5)

        # Verifying the login has failed
        invalidEmailAlertText = loginPage.getInvalidEmailAlertText().text
        assert("These credentials do not match our records." in invalidEmailAlertText)

        #dashboardPage.getUserManagementTab().click()
        #time.sleep(5)
        #dashboardPage.getPermissionsTab().click()
        #dashboardPage.getLogoutTab().click()
        #print("Google search completed!!!")
        #self.driver.refresh()

        # Step-1: Open the Support Ticketing URL
        # Step-2: Click on the "Login" button
        # Step-3: Enter the email
        # Step-4: Enter the password
        # Step-5: Check the remember me checkbox
        # Step-6: Click on the "Login" button

    #@pytest.fixture(params=[("admin@admin.com", "password"), ("kkaiser.eco@gmail.com", "password")])
    @pytest.fixture(params=LoginPageData.test_loginPage_data_invalid_email)
    def getUserData(self, request):
        return request.param