from pageObjects.BasePage import BasePage
from pageObjects.ElementsPage import ElementsPage
from utilities.readProperties import ReadConfig
import time


class Test_Alerts:
    url = ReadConfig.getApplicationURL()

    def test_alerts(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickElements()

        self.ep = ElementsPage(self.driver)
        self.ep.setUsername("jaydee9419")
        self.ep.clickSearch()

        self.ep.getUserInfo()
