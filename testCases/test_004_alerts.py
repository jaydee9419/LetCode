from pageObjects.BasePage import BasePage
from pageObjects.AlertsPage import AlertsPage
from utilities.readProperties import ReadConfig
import time


class Test_Alerts:
    url = ReadConfig.getApplicationURL()

    def test_alerts(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickAlerts()

        self.ap = AlertsPage(self.driver)
        self.ap.clickSimple()
        self.ap.clickConfirm()
        self.ap.clickPrompt()
        self.ap.clickModern()
        time.sleep(2)

