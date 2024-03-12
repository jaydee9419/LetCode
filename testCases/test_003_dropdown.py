from pageObjects.BasePage import BasePage
from pageObjects.DropDownPage import DropDownPage
from utilities.readProperties import ReadConfig
import time


class Test_DropDrown:
    url = ReadConfig.getApplicationURL()

    def test_dropdown(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickDropDown()

        self.ddp = DropDownPage(self.driver)
        self.ddp.selectFruit()
        self.ddp.selectHeros()
        self.ddp.selectLanguage()
        self.ddp.getCountries()
        time.sleep(5)
