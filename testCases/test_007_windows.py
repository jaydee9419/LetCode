from pageObjects.BasePage import BasePage
from pageObjects.WindowsPage import WindowsPage
from utilities.readProperties import ReadConfig
import time


class Test_Alerts:
    url = ReadConfig.getApplicationURL()

    def test_alerts(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickWindows()

        self.wp = WindowsPage(self.driver)
        self.wp.clickHomePageButton()

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickWindows()

        self.wp = WindowsPage(self.driver)
        self.wp.clickMultiplewindowsButton()


