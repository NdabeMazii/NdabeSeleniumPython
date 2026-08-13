from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class login_page:

    username_id = "login-email"
    password_id = "login-password"
    login_button_id = "login-submit"

    def __init__(self,driver):
        self.driver = driver

    def getUsername(self,username):
        wait = WebDriverWait(self.driver, 10)
        wait.until(self.driver.find_element(By.ID,self.username_id)).send_keys(username)

    def getPassword(self,password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(self.driver.find_element(By.ID,self.password_id)).send_keys(password)

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(self.driver.find_element(By.ID,self.login_button_id)).click()