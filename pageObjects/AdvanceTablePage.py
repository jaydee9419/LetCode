from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

class AdvanceTablePage:
    drop_options_xpath = "//select[@name='advancedtable_length']"

    def __init__(self, driver):
        self.driver = driver

    def clickOptions(self):
        dropdown_options = self.driver.find_element(By.XPATH, self.drop_options_xpath)

        option = Select(dropdown_options)
        option.select_by_value("10")

