from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os

class WaitPage:
    btn_wait_xpath = "//button[@id='accept']"


    def __init__(self, driver):
        self.driver = driver

    def clickWait(self):
        self.driver.find_element(By.XPATH, self.btn_wait_xpath).click()

        try:
            # Wait for the alert to be present (adjust timeout as needed)
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # Switch to the alert and perform actions if needed
            alert = self.driver.switch_to.alert
            print("Alert text: ", alert.text)

            # Accept the alert (you can also dismiss it with alert.dismiss())
            alert.accept()

        except:
            print("Unable to locate the alert window")

