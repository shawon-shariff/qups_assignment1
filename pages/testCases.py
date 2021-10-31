from selenium.webdriver.common.keys import Keys
class testCase():
    def __init__(self,driver):
        self.driver = driver

        #task 1 and 2 locators : Creating Two task
        self.createTaskBtn = "AppHeaderNewTaskButton__button__text"
        self.clickToEnter_by_name = "SmartTypeTextField"
        self.Xpath = "/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div/div/div"
        self.addTaskBtn = "/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button"
        self.Xpath_for_notes = "/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div[3]/div[2]/div/div/textarea"
        self.nextWeekXpath = "/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div[2]/div[2]/button[4]"

        #task 3 locators: Adding a subtask
        self.clickFriday = "//*[@id='root']/div[2]/div[3]/div/section/div/article[1]/div[1]/div[2]/article/div/div/div/div/div/div[1]/div[1]/div[1]"
        self.addSub = "SubTaskItem__textField"
        # self.subTaskName = "/html/body/div[6]/div/div/div[3]/div/div/article/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[6]/div/article"

        #task 4 locators: Creating List
        self.clickPlusBtn = "//*[@id='root']/div[2]/div[1]/div[3]/nav/ul/li[3]/div[1]/div[2]/div/button[2]"
        self.enterListName = "//*[@id='app-sidebar-modal-28']"
        self.clickCreate = "/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button[2]"

        #task 5 locators: Adding items
        self.clickMyCreatedList = "//*[@id='root']/div[2]/div[1]/div[3]/nav/ul/li[3]/div[2]/ul/li[4]/a/div[2]"
        self.itemAdd = "//*[@id='root']/div[2]/div[3]/div/section/article[1]/div[2]/form/div/div/div[2]/div/div/div[2]/div/div/div/div"
        self.itemSubmit = "//*[@id='root']/div[2]/div[3]/div/section/article[1]/div[2]/form/button"

        #task 6 locators: Changing theme
        self.settingBtn = "//*[@id='root']/div[2]/header/div/div/div[3]/button"
        self.themeBtn = "/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[5]"
        self.darkTheme = "/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[4]/div/div/div/form/div[3]/div[1]/label"

        #task 7 locators: Notification window
        self.notificationBtn = "//*[@id='root']/div[2]/header/div/div/button[2]"
        self.updatesBtn = "/html/body/div[6]/div/div/div[1]/div/ul/li[1]/button/span"

        #task 8 locators : Enable Multiple selection option
        self.moreOptions = "//*[@id='root']/div[2]/div[3]/div/div/div/div/div/div[2]/div[2]/button[3]"
        self.selectMultiple = "/html/body/div[6]/div/div/div/div[2]/button"

        #task 9 locators: Creating tag
        self.createTagBtn = "//*[@id='root']/div[2]/div[1]/div[3]/nav/ul/li[4]/div[1]/div[2]/button[2]"
        self.noTnx = "PremiumPage2__dismissButton"

        #task 10 locators: Signing Out
        self.myProfileBtn = "/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[1]"
        self.signOutBtn = "/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[8]/div/div/div/button[3]"


    def createTask(self):
        self.driver.find_element_by_class_name(self.createTaskBtn).click()
        self.driver.find_element_by_xpath(self.Xpath).send_keys("My Daily Task")
        self.driver.find_element_by_xpath(self.addTaskBtn).click()
        print("My Daily Task...Done")

    def creatTask_2(self):
        self.driver.find_element_by_class_name(self.createTaskBtn).click()
        self.driver.find_element_by_xpath(self.Xpath).send_keys("My Friday Task")
        self.driver.find_element_by_xpath(self.Xpath_for_notes).send_keys("Hangout with friends")
        self.driver.find_element_by_xpath(self.nextWeekXpath).click()
        self.driver.find_element_by_xpath(self.addTaskBtn).click()
        print("My Friday Task...Done")

    def addSubTask(self):
        self.driver.find_element_by_xpath(self.clickFriday).click()
        self.driver.find_element_by_class_name(self.addSub).send_keys("Wake up early")
        print("sub-task included...Done")

    def createList(self):
        self.driver.find_element_by_xpath(self.clickPlusBtn).click()
        self.driver.find_element_by_xpath(self.enterListName).send_keys("My Shopping Lists")
        self.driver.find_element_by_xpath(self.clickCreate).click()
        print("Creating a list...Done")

    def itemAddOnList(self):
        self.driver.find_element_by_xpath(self.clickMyCreatedList).click()

        self.driver.find_element_by_xpath(self.itemAdd).send_keys("T-shirt")
        self.driver.find_element_by_xpath(self.itemSubmit).click()
        print("Adding item on list...Done")

    def changeTheme(self):
        self.driver.find_element_by_xpath(self.settingBtn).click()
        self.driver.find_element_by_xpath(self.themeBtn).click()
        self.driver.find_element_by_xpath(self.darkTheme).click()
        print("Theme changed to Dark..Done")

    def checkNotifications(self):
        self.driver.find_element_by_xpath(self.notificationBtn).click()
        self.driver.find_element_by_xpath(self.updatesBtn).click()
        print("Enable Notification Window...Done")

    def multipleSelectionOption(self):
        self.driver.find_element_by_xpath(self.clickMyCreatedList).click()
        self.driver.find_element_by_xpath(self.moreOptions).click()
        self.driver.find_element_by_xpath(self.selectMultiple).click()
        print("Enable Multiple Selection Option...Done")

    def createTag(self):
        self.driver.find_element_by_xpath(self.createTagBtn).click()
        self.driver.find_element_by_class_name(self.noTnx).click()
        print("Creating Tags...Done")

    def signingOut(self):
        self.driver.find_element_by_xpath(self.settingBtn).click()
        self.driver.find_element_by_xpath(self.myProfileBtn).click()
        self.driver.find_element_by_xpath(self.signOutBtn).click()
        print("Signing Out Successfully... Done")


