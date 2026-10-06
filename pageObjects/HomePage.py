# from selenium.webdriver.common.by import By
#
# class HomePage:
#     lnk_myaccount_xpath = "//span[normalize-space()='My Account']"
#     lnk_register_xpath = "//a[normalize-space()='Register']"
#     lnk_login_linktext = "link=Login"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def clickMyAccount(self):
#         self.driver.click( self.lnk_myaccount_xpath)
#
#     def clickRegister(self):
#         self.driver.click(self.lnk_register_xpath)
#
#     def clickLogin(self):
#         self.driver.click( self.lnk_login_linktext)






from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():
    lnk_myaccount_xpath = "//span[normalize-space()='My Account']"
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_myaccount_xpath))
        )
        element.click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
