class LoginPage:
    textbox_username_id = "Email"
    logout_button_xpath = "//a[contains(text(),'Logout')]"
    textbox_password_id = "Password"
    loginButton_xpath = "//button[contains(text(),'Log in')]"


    def __init__(self, driver):
        self.driver = driver


    def setUsername(self, username):
        self.driver.find_element("id",self.textbox_username_id).clear()
        self.driver.find_element("id",self.textbox_username_id).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element("id",self.textbox_password_id).clear()
        self.driver.find_element("id",self.textbox_password_id).send_keys(password)


    def clickLogin(self):
        self.driver.find_element("xpath",self.loginButton_xpath).click()


    def clickLogout(self):
        self.driver.find_element("xpath",self.logout_button_xpath).click()