from pageObjects.BasePage import BasePage
from pageObjects.DragPage import DragPage
from utilities.readProperties import ReadConfig
import time


class Test_Drag:
    url = ReadConfig.getApplicationURL()

    def test_drag(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickDrag()
        time.sleep(10)

        self.dp = DragPage(self.driver)
        self.dp.getBoundarySpace()
        self.dp.moveBox()


