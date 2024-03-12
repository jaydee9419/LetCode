from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class SampleTablePage:
    tb_prices_xpath = ("//body[1]/app-root[1]/app-simpletable[1]/section[1]/div[1]/div[1]/div[1]/div[1]"
                       "/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr/td[2]")

    tb_fname_xpath = ("//body[1]/app-root[1]/app-simpletable[1]/section[1]/div[1]/div[1]/div[1]/div[1]"
                      "/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr/td[1]")
    tb_lname_xpath = ("//body[1]/app-root[1]/app-simpletable[1]/section[1]/div[1]/div[1]/div[1]/div[1]"
                      "/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr/td[2]")

    arrow_sorting_xpath = "(//div[@class='mat-sort-header-content ng-tns-c30-0'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def getTableTotalValues(self):
        values = self.driver.find_elements(By.XPATH, self.tb_prices_xpath)

        total = 0
        for item in values:
            total += int(item.text)
        return total

    def getName(self):
        first_names = self.driver.find_elements(By.XPATH, self.tb_fname_xpath)
        last_names = self.driver.find_elements(By.XPATH, self.tb_lname_xpath)

        # Use singular variable names in the list comprehensions
        f_names = [name.text for name in first_names]
        l_names = [name.text for name in last_names]

        # Join the lists to get the full names
        full_names = [f_name + " " + l_name for f_name, l_name in zip(f_names, l_names)]

        # Print or return the result as needed
        for full_name in full_names:
            print(full_name)
            return full_name

    def sortingTableData(self):
        sort = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.arrow_sorting_xpath))
        )
        sort.click()
        print("Now list is ascending in order")
        time.sleep(1)
        sort.click()
        print("Now list is descending in order")
        time.sleep(1)
        sort.click()
        print("Now list in normal")
        time.sleep(1)


