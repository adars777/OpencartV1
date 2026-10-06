from pageObjects.AccountLoginPage import AccountLoginPage
from pageObjects.HomePage import HomePage
import os
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest

class Test_002_AccountLogin:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_account_login(self,setup):
        self.logger.info("********** test_002_AccountLogin Started *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(" ************ Launching Application *************")
        self.driver.maximize_window()


        self.hp = HomePage(self.driver)
        self.logger.info("****** Clicking on My Account -> Login *******")
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        # print("this isthe eemail: ", self.email)
        # print("this is the password: ", self.password)

        self.logger.info("****** Providing customer details for Login ********")
        self.loginpage = AccountLoginPage(self.driver)
        self.loginpage.setEmail(self.email)
        self.loginpage.setPassword(self.password)
        self.loginpage.clickLogin()
        self.targetPage = self.loginpage.isMyAccountpageExists()

        if self.targetPage==True:
            self.logger.info(" *********** Logging In ************")
            self.logger.info("*********** Account Login is Passed **************")
            assert True

        else:
            self.logger.error(" *********** Account Login is Failed! ************")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" +"test_account_login.png")
            assert False
        self.logger.info("*************** test_002_AccountLogin Finished ***************\n \n")
        self.driver.close()

