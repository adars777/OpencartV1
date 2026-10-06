from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyAccountPage():

    lnk_logout_xpath = "//a[@class='dropdown-item'][normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        wait = WebDriverWait(self.driver, 10)
        logout = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.lnk_logout_xpath))
        )
        logout.click()