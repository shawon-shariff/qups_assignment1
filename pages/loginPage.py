class loginPage():
    def __init__(self,driver):
        self.driver = driver
        self.select_login_google_class_name = "AppLoginButton--google"
        self.username_by_id = "identifierId"
        self.username_next_clickbtn_id = "identifierNext"
        self.password_by_name = "password"
        self.password_next_clickbtn_id = "passwordNext"


    def select_google(self):
        self.driver.find_element_by_class_name(self.select_login_google_class_name).click()

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_by_id).clear()
        self.driver.find_element_by_id(self.username_by_id).send_keys(username)
        self.driver.find_element_by_id(self.username_next_clickbtn_id).click()

    def enter_password(self,password):
        self.driver.find_element_by_name(self.password_by_name).clear()
        self.driver.find_element_by_name(self.password_by_name).send_keys(password)

    def sign_in(self):
        self.driver.find_element_by_id(self.password_next_clickbtn_id).click()

