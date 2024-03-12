from pageObjects.BasePage import BasePage
from pageObjects.DragAndDropPage import DragAndDropPage
from utilities.readProperties import ReadConfig
import time


class Test_DragAndDrop:
    url = ReadConfig.getApplicationURL()

    def test_draganddrop(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickDrop()

        self.dadp = DragAndDropPage(self.driver)
        self.dadp.setDragAndDrop()
