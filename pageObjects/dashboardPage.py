from selenium.webdriver.common.by import By

class DashboardPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Defining the locators in Dashboard section
    loginConfirmationText = (By.XPATH, "(//div[@class='card-header'])")

    # Defining the locators in Vertical Menu
    userManagementTab = (By.XPATH, "//a[@class='nav-link  nav-dropdown-toggle']")
    permissionsTab = (By.XPATH, "//a[@href='https://ticketing.learnsqa.com/admin/permissions']")
    logoutTab = (By.XPATH, "//nav//li[@class='nav-item']//a[@href='#']")

    # Methods for obtaining locators in the test script
    def getLoginConfirmationText(self):
        return self.driver.find_element(*DashboardPage.loginConfirmationText)

    def getUserManagementTab(self):
        return self.driver.find_element(*DashboardPage.userManagementTab)
    def getPermissionsTab(self):
        return self.driver.find_element(*DashboardPage.permissionsTab)
    def getLogoutTab(self):
        return self.driver.find_element(*DashboardPage.logoutTab)