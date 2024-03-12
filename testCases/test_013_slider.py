from pageObjects.BasePage import BasePage
from pageObjects.SliderPage import SliderPage
from utilities.readProperties import ReadConfig
import time


class Test_SliderPage:
    url = ReadConfig.getApplicationURL()

    def test_sliderpage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickSlider()

        self.sp = SliderPage(self.driver)
        self.sp.getSliderSize()

        time.sleep(3)



