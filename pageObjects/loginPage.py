from selenium.webdriver.common.by import By
from pageObjects.dashboardPage import DashboardPage


class LoginPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Defining the locators in Login page
    emailField = (By.XPATH, "(//input[@id='email'])")
    passwordField = (By.XPATH, "(//input[@id='password'])")
    rememberMeCheckbox = (By.XPATH, "(//label[normalize-space()='Remember me'])")
    loginButton = (By.XPATH, "(//button[normalize-space()='Login'])")
    invalidEmailAlertText = (By.XPATH, "//div[@class='invalid-feedback']")
    wrongPasswordAlertText = (By.XPATH, "//div[@class='invalid-feedback']")

    # Methods for obtaining locators in the test script
    def getEmailField(self):
        return self.driver.find_element(*LoginPage.emailField)
    def getPasswordField(self):
        return self.driver.find_element(*LoginPage.passwordField)
    def getRememberMeChcekbox(self):
        return self.driver.find_element(*LoginPage.rememberMeCheckbox)
    def getLoginButton(self):
        #return self.driver.find_element(*LoginPage.loginButton)
        self.driver.find_element(*LoginPage.loginButton).click()
        dashboardPage = DashboardPage(self.driver)
        #verticalMenu = VerticalMenu(self.driver)
        return dashboardPage
    def getInvalidEmailAlertText(self):
        return self.driver.find_element(*LoginPage.invalidEmailAlertText)
    def getWrongPasswordlAlertText(self):
        return self.driver.find_element(*LoginPage.wrongPasswordAlertText)