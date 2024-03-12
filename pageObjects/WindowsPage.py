from selenium.webdriver.common.by import By
import time

class WindowsPage:
    btn_homepage_xpath = "//button[@id='home']"
    btn_multiplewindow_xpath = "//button[@id='multi']"

    def __init__(self, driver):
        self.driver = driver

    def clickHomePageButton(self):
        self.driver.find_element(By.XPATH, self.btn_homepage_xpath).click()
        all_windows = self.driver.window_handles

        child_window_handle = all_windows[1]
        self.driver.switch_to.window(child_window_handle)

        print("Child Window Title:", self.driver.title)

        self.driver.switch_to.window(all_windows[0])
        self.driver.close()
        time.sleep(2)

        # Close the child window
        self.driver.switch_to.window(child_window_handle)
        self.driver.close()
        time.sleep(2)


    def clickMultiplewindowsButton(self):
        self.driver.find_element(By.XPATH, self.btn_multiplewindow_xpath).click()
        all_windows = self.driver.window_handles

        child_window_handle = all_windows[1]
        self.driver.switch_to.window(child_window_handle)

        print("Child Window Title:", self.driver.title)

        self.driver.switch_to.window(all_windows[0])
        print("Parent Window Title:", self.driver.title)


        time.sleep(2)

        # Quit the WebDriver
        self.driver.quit()
