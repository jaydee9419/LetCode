from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class SliderPage:
    bar_slider_xpath = "//input[@id='generate']"
    btn_countries_xpath = "//button[normalize-space()='Get Countries']"
    txt_list_xpath = "//p[@class='has-text-primary-light']"

    def __init__(self, driver):
        self.driver = driver

    def getSliderSize(self):
        slider = self.driver.find_element(By.XPATH, self.bar_slider_xpath)
        print(slider.size)

        slider_width = slider.size['width']

        # Set the desired position (adjust as needed)
        desired_position = 25  # Example: 25% position

        # Calculate the horizontal offset based on the desired position
        offset = int(slider_width * desired_position / 100)

        # Use ActionChains to move the slider
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform()

        btn = self.driver.find_element(By.XPATH, self.btn_countries_xpath)
        btn.click()

        list_of_countries = self.driver.find_element(By.XPATH, self.txt_list_xpath)

        print(list_of_countries.text)

