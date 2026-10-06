from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import os
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger= LogGen.loggen() #for logging


    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.logger.info("*************** test_001_AccountRegistration Started *****************")
        # print("BASE URL =", repr(self.baseURL))
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(" ****** Launching Application ********")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("***** Clicking on MyAccount -> Register *****")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("***** Providing customer details for registration *****")
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("Jhon")
        self.regpage.setLastName("Canedy")
        self.email = randomString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("Jhon@123")
        self.regpage.setPrivacyPolicy()
        self.regpage.checkContinue()

        self.confMsg = self.regpage.getConfirmationmsg()
        # print(self.confMsg)

        if self.confMsg=='Your Account Has Been Created!':
            self.logger.info("***** Account Registration is Passed! *****")
            self.driver.close()
            assert True

        else:
            self.logger.error("***** Account Registration is Failed! *****")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
            self.driver.close()
            assert False

        self.logger.info("*************** test_001_AccountRegistration Finished ***************\n \n")


