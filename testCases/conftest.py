import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def setup2():
    options = Options()
    options.add_experimental_option('prefs', {'profile.managed_default_content_settings.javascript': 2})

    driver = webdriver.Chrome(options=options)
    return driver

def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'


# It is hooking for delete/Modify Environment info to HTML Report
pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

