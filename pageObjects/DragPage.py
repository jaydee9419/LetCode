from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class DragPage:
    box_space_xpath = "//div[@class='example-boundary']"
    box_drag_xpath = "//h3[@id='header']"

    def __init__(self, driver):
        self.driver = driver

    def getBoundarySpace(self):
        place = self.driver.find_element(By.XPATH, self.box_space_xpath)
        print(place.size)

    def moveBox(self):
        draggable_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.box_drag_xpath))
        )

        place = self.driver.find_element(By.XPATH, self.box_space_xpath)
        container_size = place.size
        # Use ActionChains to perform the drag and drop within the 400x400 space
        actions = ActionChains(self.driver)
        actions.click_and_hold(draggable_element)

        # Move the draggable element within the 400x400 space (adjust the offsets as needed)
        actions.move_by_offset(45, 45)
        actions.release()
        actions.perform()
        time.sleep(3)

        # Close the browser
        self.driver.quit()
