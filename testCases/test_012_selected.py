from pageObjects.BasePage import BasePage
from pageObjects.SelectedPage import SelectPage
from utilities.readProperties import ReadConfig
import time


class Test_SelectPage:
    url = ReadConfig.getApplicationURL()

    def test_selectpage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickSelect()

        self.sp = SelectPage(self.driver)
        self.sp.getSelectItems()

        time.sleep(5)


