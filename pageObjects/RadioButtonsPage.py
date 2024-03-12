from selenium.webdriver.common.by import By
import time

class RadioButtonsPage:
    btn_first_xpath = "//div[@class='card-content']//div[1]//div[1]//label/input"
    btn_second_xpath = "//div[@class='card-content']//div[2]//div[1]//label/input"
    btn_third_xpath = "//div[@class='card-content']//div[3]//div[1]//label/input"
    btn_fourth_xpath = "//div[@class='card-content']//div[4]//div[1]//label/input"
    btn_fifth_xpath = "//div[@class='card-content']//div[5]//div[1]//label/input"

    def __init__(self, driver):
        self.driver = driver

    def clickSelectAnyOne(self):
        buttons = self.driver.find_elements(By.XPATH, self.btn_first_xpath)
        count = 3
        while count >= 1:
            for item in buttons:
                item.click()
                print(item.get_attribute("id"))
                count -= 1
                time.sleep(1)

    def clickSelectOnlyOne(self):
        buttons = self.driver.find_elements(By.XPATH, self.btn_second_xpath)
        count = 2
        while count >= 1:
            for item in buttons:
                item.click()
                print(item.get_attribute("id"))
                count -= 1
                time.sleep(1)

    def clickBothButtons(self):
        buttons = self.driver.find_elements(By.XPATH, self.btn_third_xpath)
        count = 4
        while count >= 1:
            for item in buttons:
                item.click()
                print(item.get_attribute("id"))
                count -= 1
                time.sleep(1)

    def checkIsSelected(self):
        buttons = self.driver.find_elements(By.XPATH, self.btn_fourth_xpath)
        for item in buttons:
            if item.is_selected():
                print("Pre-selected Radio Button is: ", item.get_attribute("id"))
                time.sleep(1)


    def checkEnableStatus(self):
        buttons = self.driver.find_elements(By.XPATH, self.btn_fifth_xpath)
        for item in buttons:
            if item.is_enabled():
                print("This Radio button is enabled to click: ", item.get_attribute("id"))

            else:
                print("This Radio button is disabled to click: ", item.get_attribute("id"))


