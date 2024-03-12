import os.path

from pageObjects.BasePage import BasePage
from pageObjects.ClickPage import ClickPage
from utilities.readProperties import ReadConfig
import time


class Test_Click:
    url = ReadConfig.getApplicationURL()

    def test_click(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickClicks()

        self.cp = ClickPage(self.driver)
        self.cp.clickHome()
        self.cp.getLocation()
        self.cp.getColor()
        self.cp.getSize()
        self.cp.checkEnableStatus()
        self.cp.checkandHold()

        self.driver.quit()








