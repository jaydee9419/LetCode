from pageObjects.BasePage import BasePage
from pageObjects.WaitPage import WaitPage
from utilities.readProperties import ReadConfig
import time


class Test_FilesPage:
    url = ReadConfig.getApplicationURL()

    def test_waitpage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickWait()

        self.wp = WaitPage(self.driver)
        self.wp.clickWait()
        time.sleep(3)
