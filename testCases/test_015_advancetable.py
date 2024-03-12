from pageObjects.BasePage import BasePage
from pageObjects.AdvanceTablePage import AdvanceTablePage
from utilities.readProperties import ReadConfig
import time


class Test_AdvanceTablePage:
    url = ReadConfig.getApplicationURL()

    def test_advancetablepage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickAdvanceTable()

        self.atp = AdvanceTablePage(self.driver)
        self.atp.clickOptions()

        time.sleep(3)
