import pytest
from selenium.webdriver import Keys
import time
from pageObjects.addTicketPage import AddTicketPage
from testData.addTicketPageData import AddTicketPageData
from utilities.BaseClass import BaseClass

class TestAddASupportTicket(BaseClass):
    def test_addASupportTicket(self, getUserData):
        log = self.getLogger()
        log.info("Step-1: Opening the Ticketing Page")
        # Instantiating the AddTicketPage class passing the current webdriver object
        addTicketPage = AddTicketPage(self.driver)
        time.sleep(3)

        # Step-2: Enter the UserName
        log.info("Step-2: Entering the User Name")
        addTicketPage.getYourNameField().send_keys(getUserData["Your Name"])
        time.sleep(3)

        # Step-3: Enter the UserEmail
        log.info("Step-3: Entering the User Email")
        addTicketPage.getYourEmailField().send_keys(getUserData["Your Email"])
        time.sleep(3)

        # Step-4: Enter the Title
        log.info("Step-4: Entering the Title")
        addTicketPage.getTitleField().send_keys(getUserData["Title"])
        time.sleep(3)

        # Step-5: Enter the Content
        log.info("Step-5: Entering the Content")
        addTicketPage.getContentField().send_keys(getUserData["Content"])
        time.sleep(3)

        # Step-6: Click on the Submit button
        log.info("Step-6: Clicking the Submit Button")
        addTicketPage.getSubmitButton()
        time.sleep(5)

        # Verifying the ticket has submitted successfully
        successMassageText = addTicketPage.getSuccesMassageText().text
        assert ("Your ticket has been submitted, we will be in touch. You can view ticket status here" in successMassageText)

    @pytest.fixture(params=AddTicketPageData.test_addASupportTicket_data)
    def getUserData(self, request):
        return request.param