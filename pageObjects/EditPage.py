from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class EditPage:
    txt_name_xpath = "//input[@id='fullName']"
    txt_value_xpath = "//input[@id='getMe']"
    txt_clear_xpath = "//input[@id='clearMe']"
    txt_enable_xpath = "//input[@id='noEdit']"

    def __init__(self, driver):
        self.driver = driver

    def setName(self):
        name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_name_xpath))
        )
        name.send_keys("Rakesh")

    def getValue(self):
        value = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_value_xpath))
        )
        return value.get_attribute("value")

    def clearData(self):
        data = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_clear_xpath))
        )
        data.clear()

    def ckeckEnableStatus(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_enable_xpath))
        )
        self.driver.execute_script(
            "window.scrollBy(0, -window.innerHeight / 2 + "
            "arguments[0].getBoundingClientRect().top + arguments[0].clientHeight / 2);",
            field
        )
        return field.is_enabled()



