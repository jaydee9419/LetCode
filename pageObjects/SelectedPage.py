from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class SelectPage:
    lst_items_xpath = "//div[@id='container']/div"

    def __init__(self, driver):
        self.driver = driver

    def getSelectItems(self):
        list_of_items = self.driver.find_elements(By.XPATH, self.lst_items_xpath)

        for i in range(0, len(list_of_items), 4):
            try:
                actions = ActionChains(self.driver)
                actions.key_down(Keys.CONTROL)
                actions.click(list_of_items[i])
                actions.key_up(Keys.CONTROL)
                actions.perform()
            except Exception as e:
                print(f"Exception: {e}")

        for item in list_of_items:
            if item.get_attribute("class") == "ui-selectable ui-selected":
                print(f"Item {item.text} is selected: {item.is_selected()}")
