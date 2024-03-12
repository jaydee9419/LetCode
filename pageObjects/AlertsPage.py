import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class AlertsPage:
    btn_simple_xpath = "//button[@id='accept']"
    btn_confirm_xpath = "//button[@id='confirm']"
    btn_prompt_xpath = "//button[@id='prompt']"
    btn_modern_xpath = "//button[@id='modern']"
    btn_close_xpath = "//button[@aria-label='close']"

    def __init__(self, driver):
        self.driver = driver

    def clickSimple(self):
        simple = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_simple_xpath))
        )
        simple.click()
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def clickConfirm(self):
        confirm = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_confirm_xpath))
        )
        confirm.click()
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()

    def clickPrompt(self):
        confirm = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_prompt_xpath))
        )
        confirm.click()
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.send_keys("Hello World")
        time.sleep(2)
        alert.accept()

    def clickModern(self):
        confirm = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_modern_xpath))
        )
        confirm.click()
        time.sleep(1)

        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_close_xpath))
        )
        close.click()
        time.sleep(1)

