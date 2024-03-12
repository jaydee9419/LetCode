from pageObjects.BasePage import BasePage
from pageObjects.ShadowDOMPage import ShadowDOMPage
from utilities.readProperties import ReadConfig
import time


class Test_ShadowDOMPage:
    url = ReadConfig.getApplicationURL()

    def test_shadowdompage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickShadowDOM()

        self.sdp = ShadowDOMPage(self.driver)
        self.sdp.set_fname()
        self.sdp.set_lname()
        self.sdp.set_email()

        time.sleep(10)
