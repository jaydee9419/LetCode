from pageObjects.BasePage import BasePage
from pageObjects.SortPage import SortPage
from utilities.readProperties import ReadConfig
import time


class Test_SortPage:
    url = ReadConfig.getApplicationURL()

    def test_sortpage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickSort()

        self.sp = SortPage(self.driver)
        self.sp.setAllItemsFromSourceToTarget()
        time.sleep(5)

