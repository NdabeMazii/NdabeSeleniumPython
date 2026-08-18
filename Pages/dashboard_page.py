from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class dashboard_page:

    welcome_back_xpath = "//h2"

    def __init__(self, driver):
        self.driver = driver

    def verify_dashboard_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(self.driver.find_element(By.XPATH,self.welcome_back_xpath).is_displayed())