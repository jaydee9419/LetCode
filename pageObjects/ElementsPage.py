from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ElementsPage:
    input_name_xpath = "//input[@name='username']"
    btn_search_xpath = "//button[@id='search']"

    img_profile_xpath = "//img[@alt='Placeholder image']"
    txt_name_xpath = "(//p[@class='title is-4'])[1]"
    txt_repo_xpath = "//div[@class='field is-grouped is-grouped-multiline']//div[1]//div[1]"
    txt_gist_xpath = "//div[@class='field is-grouped is-grouped-multiline']//div[2]//div[1]"
    txt_followers_xpath = "//div[@class='field is-grouped is-grouped-multiline']//div[3]//div[1]"
    lnk_links_xpath = "//div[@class='column is-7-desktop is-8-tablet']//li"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, uname):
        self.driver.find_element(By.XPATH, self.input_name_xpath).send_keys(uname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def getUserInfo(self):
        img = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.img_profile_xpath))
        )
        if img.is_displayed():
            print("===================")
            print(img.is_displayed(), "We can see profile photo")
        else:
            print("===================")
            print(img.is_displayed(), "We can't see profile photo")

        name = self.driver.find_element(By.XPATH, self.txt_name_xpath)
        print("===================")
        print("Username is:", name.text)

        repo = self.driver.find_element(By.XPATH, self.txt_repo_xpath)
        gist = self.driver.find_element(By.XPATH, self.txt_gist_xpath)
        followers = self.driver.find_element(By.XPATH, self.txt_followers_xpath)
        print("===================")
        print(f"{repo.text}\n{gist.text}\n{followers.text}")
        print("===================")
        print("Below are the GitHub Links:")

        links = self.driver.find_elements(By.XPATH, self.lnk_links_xpath)
        for link in links:
            href = link.text
            print(href)



