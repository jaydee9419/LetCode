from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta


class CalendarPage:
    date_start_xpath = "//input[@class='datetimepicker-dummy-input is-datetimepicker-range']"
    date_end_xpath = "//div[@class='datepicker is-active']//div[@class='datepicker-days']/div"
    date_today_xpath = "//div[@class='datetimepicker is-primary is-datetimepicker-default is-active']//button[@type='button'][normalize-space()='Today']"
    time_hours_xpath = "//div[@class='timepicker-hours']//span[@class='timepicker-next'][normalize-space()='+']"

    def __init__(self, driver):
        self.driver = driver

    def clickStart(self):
        self.driver.find_element(By.XPATH, self.date_start_xpath).click()
        self.driver.find_element(By.XPATH, self.date_today_xpath).click()

    def clickEnd(self):
        ends = self.driver.find_elements(By.XPATH, self.date_end_xpath)


        for end in ends:
            if end.get_attribute("class") == "datepicker-date is-current-month datepicker-range-start":
                current_date_str = end.text
                print(current_date_str)
                # Assuming the date is represented as text on the web page
                current_date = datetime.strptime(current_date_str, "%m-%d-%Y")  # Adjust the format accordingly

                # Add two days to the current date
                new_date = current_date + timedelta(days=2)

                # Click on the new date (you might need to convert it back to a string based on your datepicker implementation)
                new_date_str = new_date.strftime("%m-%d-%Y")  # Adjust the format accordingly
                end.click()

                # Perform the necessary actions with the new date
                ...

                break

    def clickTime(self):
        time = self.driver.find_element(By.XPATH, self.time_hours_xpath)

        count = 2
        while count >= 1:
            time.click()
            count -= 1
