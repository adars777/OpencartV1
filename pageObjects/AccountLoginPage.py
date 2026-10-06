from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountLoginPage:
    txt_email_name = "email"
    txt_password_name = "password"
    btn_login_xpath = "//button[normalize-space()='Login']"
    msg_myAccount_xpath = "//h2[normalize-space()='My Account']"


    def __init__(self, driver):
        self.driver = driver


    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def isMyAccountpageExists(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                EC.visibility_of_element_located((By.XPATH, self.msg_myAccount_xpath))
            )
            return True
        except:
            False
