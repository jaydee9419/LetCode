from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class ClickPage:
    btn_home_xpath = "//button[@id='home']"
    btn_location_xpath = "//button[@id='position']"
    btn_color_xpath = "//button[@id='color']"
    btn_property_xpath = "//button[@id='property']"
    btn_enable_xpath = "//button[@title='Disabled button']"
    btn_hold_xpath = "//div[6]//div[1]//button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickHome(self):
        home = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_home_xpath))
        )
        home.click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)


    def getLocation(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_location_xpath))
        )
        location = element.location

        # Print the x and y coordinates
        print("X Coordinate:", location['x'])
        print("Y Coordinate:", location['y'])

    def getColor(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_color_xpath))
        )
        color = element.value_of_css_property("background-color")
        print(color)

    def getSize(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_property_xpath))
        )
        size = element.size
        print(size)

    def checkEnableStatus(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_enable_xpath))
        )
        print(element.is_enabled())

    def checkandHold(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_hold_xpath))
        )

        actions = ActionChains(self.driver)

        # Press and hold the button
        actions.click_and_hold(element).perform()

        time.sleep(1)

        # Release the button (simulate releasing the mouse click)
        actions.release().perform()

        print(element.text)



