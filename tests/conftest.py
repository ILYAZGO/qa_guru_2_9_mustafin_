import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def browser_preconfig():
    browser.config.browser_name="chrome"
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width=1920
    browser.config.window_height=1080

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    yield