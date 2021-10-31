import span as span
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from pages.loginPage import loginPage
from pages.testCases import testCase

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(120)
        cls.driver.maximize_window()

    def test_login_val(self):
        driver = self.driver
        driver.get("https://desktop.any.do/")

        #logging in
        login = loginPage(driver)
        login.select_google()
        login.enter_username("automationtest2444@gmail.com")
        login.enter_password("Automationtest@2444")
        login.sign_in()

        #task 1: Creating My daily Task
        tc001 = testCase(driver)
        tc001.createTask()

        time.sleep(3)

        #task 2: Creating My Friday Task
        tc002 = testCase(driver)
        tc002.creatTask_2()

        time.sleep(3)

        #task 3: Adding Subtask
        # tc003 = testCase(driver)
        # tc003.addSubTask()
        #
        #task 4: Creating List
        tc004 = testCase(driver)
        tc004.createList()

        time.sleep(3)

        #task 5: Adding Items
        tc005 = testCase(driver)
        tc005.itemAddOnList()

        time.sleep(3)

        #task 6: Changing Theme
        tc006 = testCase(driver)
        tc006.changeTheme()
        time.sleep(3)

        #task 7: Notification Window
        tc007 = testCase(driver)
        tc007.checkNotifications()
        time.sleep(3)

        #task 8: Multiple Selection Option
        tc008 = testCase(driver)
        tc008.multipleSelectionOption()
        time.sleep(3)


        #task 9: Creating Tags
        # tc009 = testCase(driver)
        # tc009.createTag()
        # time.sleep(3)

        # task 10: Signing Out
        tc010 = testCase(driver)
        tc010.signingOut()

    # @classmethod
    # def tearDownClass(cls):
    #      cls.driver.close()
    #      cls.driver.quit()
    #      print("Task COmpleted")


