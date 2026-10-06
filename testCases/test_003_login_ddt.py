import time
from pageObjects.HomePage import HomePage
from pageObjects.AccountLoginPage import AccountLoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    path = os.path.abspath(os.curdir)+"\\testData\\Opencart_LoginData.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("****** Starting test_003_login_Data Driven *****")
        self.rows= XLUtils.getRowCount(self.path,'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)   #homepage page object class
        self.lp = AccountLoginPage(self.driver)    #loginPage page object class
        self.ma = MyAccountPage(self.driver)    # MyAccount page object class

        for r in range(2, self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path, "Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1",r,2)
            self.exp = XLUtils.readData(self.path, "Sheet1",r,3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(1)
            self.targetPage = self.lp.isMyAccountpageExists()

            if self.exp == "Valid":
                if self.targetPage==True:
                    lst_status.append("Pass")
                    # print("this TC is passed and going to click logout button.")
                    self.hp.clickMyAccount()
                    self.ma.clickLogout()
                else:
                    lst_status.append("Fail")

            elif self.exp=="Invalid":
                if self.targetPage==True:
                    lst_status.append("Fail")
                    # print("this TC is Failed and going to click logout button.")
                    self.hp.clickMyAccount()
                    self.ma.clickLogout()
                else:
                    lst_status.append("Pass")


        #final validation
        if "Fail" not in lst_status:
             assert True

        else:
            assert False

        self.driver.close()
        # print('this is the result of the data driven test data: ', lst_status)
        self.logger.info("************** End of test_003_login_Data_Driven **************")


