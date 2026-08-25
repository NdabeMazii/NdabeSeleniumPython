import allure
import pytest
from selenium.webdriver.common import driver_finder

from Pages.home_page import home_page
from Pages.login_page import login_page
from Utils import config_properties
from Utils.launch_browser import launch_browser
from Utils.login_function import login


class TestLogin:

    dev_url = config_properties.ReadConfig_CommonDetails().getDevUrl()
    username = config_properties.ReadConfig_CommonDetails().getUsername()
    password = config_properties.ReadConfig_CommonDetails().getPassword()
    invalid_username = config_properties.ReadConfig_CommonDetails().getInvalidUsername()
    invalid_password = config_properties.ReadConfig_CommonDetails().getInvalidPassword()


    @pytest.mark.sanity
    def test_valid_login(self, setup):

        self.driver = setup
        self.driver.get(self.dev_url)

        home = home_page(self.driver)
        home.click_main_login_button()

        login = login_page(self.driver)
        login.getUsername(self.username)
        login.getPassword(self.password)
        login.clickLoginButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Login positive", attachment_type=allure.attachment_type.PNG)



