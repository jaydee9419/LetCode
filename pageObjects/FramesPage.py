from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FramesPage:
    frm_outerframe_xpath = "//iframe[@id='firstFr']"
    input_fname_xpath = "//input[@placeholder='Enter name']"
    input_lname_xpath = "//input[@name='lname']"

    frm_innerframe_xpath = "//iframe[@class='has-background-white']"
    input_mail_xpath = "//input[@name='email']"

    def __init__(self, driver):
        self.driver = driver

    def switchOuterFrame(self):
        outerframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.frm_outerframe_xpath))
        )
        self.driver.switch_to.frame(outerframe)

    def switchInnerFrame(self):
        innerframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.frm_innerframe_xpath))
        )
        self.driver.switch_to.frame(innerframe)

    def setFname(self, name):
        f_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.input_fname_xpath))
        )
        f_name.send_keys(name)

    def setLname(self, name):
        l_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.input_lname_xpath))
        )
        l_name.send_keys(name)

    def setEmail(self, mail):
        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.input_mail_xpath))
        )
        email.send_keys(mail)




