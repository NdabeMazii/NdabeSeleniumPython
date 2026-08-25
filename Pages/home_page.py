from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class home_page:

    main_login_button_xpath = "//div[@class='nav-user-section']"

    def __init__(self, driver):
        self.driver = driver

    def click_main_login_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,self.main_login_button_xpath))).click()