from pageObjects.BasePage import BasePage
from pageObjects.FramesPage import FramesPage
from utilities.readProperties import ReadConfig
import time


class Test_Alerts:
    url = ReadConfig.getApplicationURL()

    def test_alerts(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickFrames()

        self.fp = FramesPage(self.driver)
        self.fp.switchOuterFrame()
        self.fp.setFname("Rakesh")
        self.fp.setLname("Mara")
        self.fp.switchInnerFrame()
        self.fp.setEmail("Rakesh@gmail.com")
        time.sleep(10)
