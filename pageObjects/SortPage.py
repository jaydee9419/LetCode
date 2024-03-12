from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class SortPage:
    box_source_xpath = "/html/body/app-root/app-sortable/section[1]/div/div/div[1]/div/div/div/div/div[1]/div/div"
    box_target_xpath = "/html/body/app-root/app-sortable/section[1]/div/div/div[1]/div/div/div/div/div[2]/div"


    def __init__(self, driver):
        self.driver = driver

    def setAllItemsFromSourceToTarget(self):
        source_elements = self.driver.find_elements(By.XPATH, self.box_source_xpath)
        target_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.box_target_xpath))
                )

        for item in source_elements:
            try:
                actions = ActionChains(self.driver)
                actions.drag_and_drop(item, target=target_element)
                actions.perform()

            except TimeoutException as e:
                print(f"TimeoutException: {e}")
