from Pages.home_page import home_page
from Pages.login_page import login_page


def login(driver, username, password):
    homeP = home_page(driver)
    loginP = login_page(driver)

    homeP.click_main_login_button()
    loginP.getUsername(username)
    loginP.getPassword(password)
    loginP.clickLoginButton()