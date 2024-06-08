from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage


class AddTicketPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Defining the locators in Login page
    loginButton = (By.XPATH, "(//a[normalize-space()='Login'])")
    yourNameField = (By.XPATH, "//input[@id='author_name']")
    yourEmailField = (By.XPATH, "//input[@id='author_email']")
    titleField = (By.XPATH, "//input[@id='title']")
    contentField = (By.XPATH, "//textarea[@id='content']")
    submitButton = (By.XPATH, "//button[@type='submit']")
    successMassageText = (By.XPATH, "//div[@role='alert']")

    # Methods for obtaining locators in the test script
    def getLoginButton(self):
        self.driver.find_element(*AddTicketPage.loginButton).click()
        loginPage = LoginPage(self.driver)
        return loginPage

    def getYourNameField(self):
        return self.driver.find_element(*AddTicketPage.yourNameField)

    def getYourEmailField(self):
        return self.driver.find_element(*AddTicketPage.yourEmailField)

    def getTitleField(self):
        return self.driver.find_element(*AddTicketPage.titleField)

    def getContentField(self):
        return self.driver.find_element(*AddTicketPage.contentField)

    def getSubmitButton(self):
        return self.driver.find_element(*AddTicketPage.submitButton).click()

    def getSuccesMassageText(self):
        return self.driver.find_element(*AddTicketPage.successMassageText)