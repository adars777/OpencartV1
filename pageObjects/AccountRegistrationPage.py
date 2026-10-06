from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountRegistrationPage:
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_password_name = "password"
    chk_policy_xpath = "//input[@name='agree']"
    btn_cont_xpath = "//button[normalize-space()='Continue']"
    text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

    def setPrivacyPolicy(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver import ActionChains

        wait = WebDriverWait(self.driver, 20)
        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, self.chk_policy_xpath)))

        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)

        # Human-like click
        actions = ActionChains(self.driver)
        actions.move_to_element(checkbox).pause(0.5).click().perform()

    def checkContinue(self):
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()

    def getConfirmationmsg(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(
                EC.element_to_be_clickable((By.XPATH, self.text_msg_conf_xpath))
            )

            return element.text

        except:
            None





