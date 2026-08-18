from Utils import config_properties

def launch_browser(driver):
    dev_url = config_properties.ReadConfig_CommonDetails().getDevUrl()
    driver.get(dev_url)
    driver.maximize_window()

    return driver
