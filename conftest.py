import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup_driver():
    options = Options()
    options.add_argument("--incognito")  # This must be set before initializing the driver
    driver = webdriver.Chrome(options=options)  # Pass options here
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")

    try:
        actions = ActionChains(driver)
        actions.move_by_offset(10, 100).click().perform()
    except:
        pass

    driver.implicitly_wait(10)
    yield driver
    driver.quit()