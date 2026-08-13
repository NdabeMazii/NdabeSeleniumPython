from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class home_page:

    main_login_button_xpath = "//div[@class='nav-user-section']"

    def __init__(self, driver):
        self.driver = driver

    def click_main_login_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(self.driver.find_element(By.XPATH,self.main_login_button_xpath).click())