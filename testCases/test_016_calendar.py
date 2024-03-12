from pageObjects.BasePage import BasePage
from pageObjects.CalendarPage import CalendarPage
from utilities.readProperties import ReadConfig
import time


class Test_CalendarPage:
    url = ReadConfig.getApplicationURL()

    def test_calendarpage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickCalendar()

        self.cp = CalendarPage(self.driver)
        self.cp.clickStart()
        time.sleep(2)
        self.cp.clickEnd()
        self.cp.clickTime()
        time.sleep(10)
