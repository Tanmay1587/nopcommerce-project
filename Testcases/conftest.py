from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

def pytest_addoption(parser): #This will get the value for CLI /Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #This will return the browser value to setup method
    return request.config.getoption("--browser")

####Paytest html reporting method####
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers module'
    config._metadata['Tester'] = 'Tanmay'


#### This is a hook for modify/delete the environment info to html report ####
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_home", None)
    metadata.pop("Plugins", None)
