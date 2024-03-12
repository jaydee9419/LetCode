from pageObjects.BasePage import BasePage
from pageObjects.RadioButtonsPage import RadioButtonsPage
from utilities.readProperties import ReadConfig
import time


class Test_Alerts:
    url = ReadConfig.getApplicationURL()

    def test_alerts(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickRadioButtons()

        self.rbp = RadioButtonsPage(self.driver)
        self.rbp.clickSelectAnyOne()
        self.rbp.clickSelectOnlyOne()
        self.rbp.clickBothButtons()
        self.rbp.checkIsSelected()
        self.rbp.checkEnableStatus()

        time.sleep(1)
