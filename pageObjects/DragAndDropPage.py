from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class DragAndDropPage:
    box_source_xpath = "//div[@id='draggable']"
    box_target_xpath = "//div[@id='droppable']"
    txt_confirm_xpath = "//p[normalize-space()='Dropped!']"

    def __init__(self, driver):
        self.driver = driver

    def setDragAndDrop(self):
        source = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.box_source_xpath))
        )
        target = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.box_target_xpath))
        )

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target)
        actions.perform()
        msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_confirm_xpath))
        )
        print(msg.text)
        time.sleep(3)
        self.driver.quit()

