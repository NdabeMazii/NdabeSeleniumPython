from selenium import webdriver


def setup(browser):

    # Initialize the WebDriver based on the browser name provided
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser.lower() == "edge":
        driver = webdriver.Edge()

    elif browser.lower() == "safari":
        driver = webdriver.Safari()

    else:
        driver = webdriver.Firefox()

    # Returning the WebDriver instance
    return driver

def pytest_addoption(parser):
    # Add a command-line option "--browser" to specify the browser
    parser.addoption("--browser")