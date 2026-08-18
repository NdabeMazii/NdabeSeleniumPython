import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):

    # Initialize the WebDriver based on the browser name provided
    if browser and browser.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser and browser.lower() == "edge":
        driver = webdriver.Edge()

    elif browser and browser.lower() == "safari":
        driver = webdriver.Safari()

    else:
        driver = webdriver.Firefox()

    # Provide the WebDriver to the test
    yield driver

    # Teardown: quit the browser after the test
    # driver.quit()


def pytest_addoption(parser):
    # Add a command-line option "--browser" to specify the browser
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")